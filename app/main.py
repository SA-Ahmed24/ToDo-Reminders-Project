# app/main.py
# Import necessary modules and classes from FastAPI and the application
from fastapi import FastAPI
from .routes import router  # Import the router instance from the routes module
from .database import init_db  # Import the database initialization function

# Create a FastAPI application instance
app = FastAPI()

# Register an event handler for the startup event
@app.on_event("startup")
def on_startup():
    init_db()  # Initialize the database when the application starts

# Include the router from the routes module, adding all the routes to the application
app.include_router(router)
