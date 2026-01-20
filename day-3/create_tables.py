from database import engine, Base
from models import Document

# Create all tables 
Base.metadata.create_all(bind=engine)

print("Document tables created succussfully")