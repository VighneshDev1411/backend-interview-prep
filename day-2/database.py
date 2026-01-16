from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://localhost/interview_prep"

# This creates connection engine , like creating a phone line to the database
engine = create_engine(DATABASE_URL)


# Create session factory ( to interact with database ), one conversation with database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get database session

# Creates a database session 
# yield -> give session to your code
# finally -> always close session ( clean up )
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()