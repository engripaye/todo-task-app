from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api import users, tasks  # ensure imports align with package

# Create DB tables if using simple startup (for dev only)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do App")

app.include_router(users.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")
