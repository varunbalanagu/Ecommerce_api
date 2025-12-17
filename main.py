# main.py
from fastapi import FastAPI
from celery import Celery
import os
from src.database import engine, Base

# 1. DATABASE INITIALIZATION
# We import models here so SQLAlchemy "sees" them to create the tables
import src.models.product
import src.models.user
import src.models.order

# This command creates all tables in PostgreSQL if they don't exist yet
Base.metadata.create_all(bind=engine)

# 2. FASTAPI APP SETUP
app = FastAPI(title="E-commerce API")

# 3. CELERY SETUP (Background Tasks)
celery_app = Celery(
    'tasks',
    broker=f"redis://{os.getenv('REDIS_HOST', 'redis')}:6379/0",
    backend=f"redis://{os.getenv('REDIS_HOST', 'redis')}:6379/0"
)

# 4. ROUTER REGISTRATION
# We link the Auth routes and Product routes here
from src.api.auth_controller import router as auth_router
from src.api.product_controller import router as product_router

app.include_router(auth_router)
app.include_router(product_router)

# 5. HEALTH CHECK ROUTE
@app.get("/")
def root():
    return {"status": "API is running", "message": "Welcome to the E-commerce API"}