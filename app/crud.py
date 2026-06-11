from app.database import tasks

def get_tasks():
    return tasks

def add_task(task):
    tasks.append(task)
    return task