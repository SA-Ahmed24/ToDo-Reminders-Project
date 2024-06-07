# app/models.py
# Importing necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating a base class for our database models
Base = declarative_base()

# Defining a class `Task` which inherits from the `Base` class
class Task(Base):
    # Specifying the name of the table in the database
    __tablename__ = "tasks"
    
    # Defining columns for the table
    # 'id' is an integer column, primary key, and indexed for fast lookups
    id = Column(Integer, primary_key=True, index=True)
    
    # 'title' is a string column, indexed for fast lookups
    title = Column(String, index=True)
    
    # 'description' is a string column, indexed for fast lookups
    description = Column(String, index=True)
    
    # 'completed' is an integer column, default value is 0 (indicating not completed)
    completed = Column(Integer, default=0)
