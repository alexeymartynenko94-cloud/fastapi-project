# storage.py
import sqlite3
from typing import List, Optional
from models import Task, TaskCreate

DB_PATH = "data/todo.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()

def get_tasks() -> List[Task]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, completed FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return [Task(id=r[0], title=r[1], description=r[2], completed=bool(r[3])) for r in rows]

def get_task(task_id: int) -> Optional[Task]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, completed FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Task(id=row[0], title=row[1], description=row[2], completed=bool(row[3]))
    return None

def create_task(task: TaskCreate) -> Task:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task.title, task.description, task.completed)
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return Task(id=task_id, **task.dict())

def update_task(task_id: int, task: TaskCreate) -> Optional[Task]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
        (task.title, task.description, task.completed, task_id)
    )
    conn.commit()
    conn.close()
    return get_task(task_id)

def delete_task(task_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
