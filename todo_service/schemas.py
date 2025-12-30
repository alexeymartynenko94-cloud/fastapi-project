from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str


class TaskView(BaseModel):
    id: int
    title: str
    completed: bool
