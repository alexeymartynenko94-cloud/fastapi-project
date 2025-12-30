from fastapi import FastAPI, HTTPException
from storage import init_db, get_tasks, get_task, create_task, update_task, delete_task
from models import Task, TaskCreate

app = FastAPI(title="ToDo Service")

init_db()

@app.get("/items", response_model=list[Task])
def read_tasks():
    return get_tasks()

@app.get("/items/{item_id}", response_model=Task)
def read_task(item_id: int):
    task = get_task(item_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/items", response_model=Task)
def add_task(task: TaskCreate):
    return create_task(task)

@app.put("/items/{item_id}", response_model=Task)
def modify_task(item_id: int, task: TaskCreate):
    updated = update_task(item_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/items/{item_id}")
def remove_task(item_id: int):
    delete_task(item_id)
    return {"detail": "Task deleted"}
