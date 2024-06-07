# app/crud.py
# Import necessary modules and classes
from sqlalchemy.orm import Session  # For handling database sessions
from .models import Task  # Import the Task model
from .schemas import TaskCreate, TaskUpdate  # Import schemas for creating and updating tasks

# Function to get a single task by ID
def get_task(db: Session, task_id: int):
    # Query the database for a task with the given ID
    return db.query(Task).filter(Task.id == task_id).first()

# Function to get multiple tasks with optional pagination
def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    # Query the database for tasks, applying offset and limit for pagination
    return db.query(Task).offset(skip).limit(limit).all()

# Function to create a new task
def create_task(db: Session, task: TaskCreate):
    # Create a new Task object with the given title and description
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)  # Add the new task to the database session
    db.commit()  # Commit the session to save the new task to the database
    db.refresh(db_task)  # Refresh the session to include the new task's data
    return db_task  # Return the newly created task

# Function to update an existing task
def update_task(db: Session, task_id: int, task: TaskUpdate):
    # Retrieve the existing task by ID
    db_task = get_task(db, task_id)
    if db_task:
        # Update the task's attributes if it exists
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        db.commit()  # Commit the session to save the changes
        db.refresh(db_task)  # Refresh the session to include the updated data
    return db_task  # Return the updated task (or None if not found)

# Function to delete a task
def delete_task(db: Session, task_id: int):
    # Retrieve the existing task by ID
    db_task = get_task(db, task_id)
    if db_task:
        # Delete the task from the database if it exists
        db.delete(db_task)
        db.commit()  # Commit the session to apply the deletion
    return db_task  # Return the deleted task (or None if not found)
