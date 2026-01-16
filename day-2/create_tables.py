from database import engine, Base
from models import User

# Create all tables 
Base.metadata.create_all(bind=engine)
print("Tables create successfully! ")

