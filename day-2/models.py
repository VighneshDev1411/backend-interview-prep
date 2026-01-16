from sqlalchemy import Column, Integer, String
from database import Base


"""
This model creates SQL table:
sqlCREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    age INTEGER NOT NULL
);
"""
class User(Base): # Inherits from base and connects to databasek, this is our database model basically
    __tablename__ = "users" # Simply as the name suggests name of the table in the database

    id = Column(Integer, primary_key=True, index=True) 
    # primary_key = True implies that is the uniques identifier for each row
    # index=  True is used for the fast lookups or like fast searches of the email it is called indexers in terms of sql
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    age=  Column(Integer, nullable=False)

