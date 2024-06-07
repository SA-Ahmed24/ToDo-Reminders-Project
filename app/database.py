# app/database.py
# Importing necessary modules from SQLAlchemy
# create_engine manages database connections
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setting the URL for the database. Here, it's an SQLite database stored in the file `test.db`
DATABASE_URL = "sqlite:///./test.db"

# Creating a SQLAlchemy engine that will interact with the database specified in DATABASE_URL
engine = create_engine(DATABASE_URL)

# Creating a configured "Session" class bound to the engine
# `autocommit=False` ensures that changes are not automatically committed to the database
# `autoflush=False` ensures that changes are not automatically flushed to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Importing the Base class from the models module
from .models import Base

# Function to initialize the database
# This function creates all the tables defined in the models module
def init_db():
    Base.metadata.create_all(bind=engine)
