from fastapi import FastAPI
from app.models import Task
from app.crud import get_tasks, add_task

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Todo API"}

@app.get("/tasks")
def fetch_tasks():
    return get_tasks()

@app.post("/tasks")
def create_task(task: Task):
    return add_task(task)