# app/schemas.py
# Importing the BaseModel from Pydantic
from pydantic import BaseModel

# Base schema class for a task, which includes a title and an optional description
class TaskBase(BaseModel):
    title: str
    description: str = None

# Schema class for creating a task, inherits from TaskBase
class TaskCreate(TaskBase):
    pass

# Schema class for updating a task, inherits from TaskBase and adds a completed field
class TaskUpdate(TaskBase):
    completed: int

# Schema class for reading a task, inherits from TaskBase and adds id and completed fields
class Task(TaskBase):
    id: int
    completed: int

    # Config class to allow ORM mode, which allows Pydantic models to work with ORMs like SQLAlchemy
    class Config:
        orm_mode = True
