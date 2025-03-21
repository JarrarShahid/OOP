# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import router

# Initialize the database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="OOP Python Showcase - FastAPI", version="1.0")

# Middleware for CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include API routes
app.include_router(router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI OOP Showcase!"}
