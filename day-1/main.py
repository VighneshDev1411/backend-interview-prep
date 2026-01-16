from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }

@app.get("/users")
def list_users(skip: int=0, limit: int=10):
    return {
        "skip": skip,
        "limit": limit, 
        "message": f"Fetching users from {skip} to {skip + limit}"
    }
