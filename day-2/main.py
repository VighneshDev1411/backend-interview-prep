from fastapi import FastAPI, Depends, HTTPException
# Depends = Dependency injection we use it for database sessions 
# HTTPException = For error handling 
from sqlalchemy.orm import Session
# Session = Type hint for database session
from typing import List

from database import get_db, engine
from models import User, Base
from schema import UserCreate, UserResponse

# Create tables on startup, creates tables automatically when app starts
# Safe to run multiple times ( only creates if not exists )
Base.metadata.create_all(bind=engine)
app = FastAPI(title="User Management API with PostgreSQL")


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    user:UserCreate = Request body (validated by Pydantic)
    db: Session = Depends(get_db) = Dependency injection 
        -> FastAPI automatically calls get_db()
        -> Gives us a database session 
        -> Closes it automatically after request
    """
    # First check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    """
    db.query(User) => Start a query on User Table
    .filter => filters as per the condition 
    .first() = get first result (or None if not found)
    """

    """
    SQL Equivalent
    SELECT * FROM users WHERE email = 'v@example.com' LIMIT 1;
    """
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = User(
        name = user.name,
        email = user.email,
        age = user.age
    )

    # Add to database, still not saved
    db.add(db_user)
    db.commit() # Save Changes 
    db.refresh(db_user) # Reload to get generated ID

    return db_user

# Get all user
@app.get("/users", response_model=List[UserResponse])
def list_users(skip: int=0, limit:int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

# READ - Get user by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    """
    Filter by ID
    .first() returns one user or None

    SQL Equivalent:
    SELECT * FROM users WHERE id = 5 LIMIT 1;
    """

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

"""
response_model=List[UserResponse]

-> Returns a list of UserResponse objects
-> FastAPI validates response matches this

db.query(User).offset(skip).limit(limit).all()
-> offset(skip) = Skip first N records
-> limit(limit) = Return max N records
-> .all() = Get all matching results as list

SQL Equivalent : 
SELECT * FROM users OFFSET 0 LIMIT 10;
"""

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    # Get existing user
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if new email is already exists (if email is being changed)

    if user_update.email != db_user.email:
        existing = db.query(User).filter(User.email == user_update.email).first()
        # First, find the user to update 
        if existing: 
            raise HTTPException(status_code=400, detail="Email already registered")
        
        """
        Only check duplicate email if email is changing.
        If email stays same, no need to check.
        """
    
    # Update fields 
    db_user.name = user_update.name
    db_user.email = user_update.email
    db_user.age = user_update.age

    """
    Update the fields 
    Object is modified in memory
    """

    """
    SQL Equivalent 

    UPDATE users 
    SET name = 'New Name', email = 'new@example.com', age = 26
    WHERE id = 1;

    """

    # Save changed 
    db.commit()
    db.refresh(db_user)
    
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Find User

    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully", "user_id": user_id}
    



# Root endpoint
@app.get("/")
def read_root():
    return {"message": "User Management API with PostgreSQL"}
