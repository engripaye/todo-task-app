from sqlalchemy.orm import Session
from app.models.task import Task
from typing import Optional


def create_task(db: Session, owner_id: int, title: str, description: Optional[str] = None):
    task = Task(title=title, description=description, owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task(db: Session, task_id: int, owner_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()


def list_tasks(db: Session, owner_id: int):
    return db.query(Task).filter(Task.owner_id == owner_id).all()


def updated_task(db: Session, task: Task, title: Optional[str] = None, description: Optional[str] = None,
                 completed: Optional[bool] = None):
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if completed is not None:
        task.completed = completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
