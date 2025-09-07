from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.task import TaskCreate, TaskOut, TaskUpdate
from app.api.dependencies import get_db, get_current_user
from app.crud.task import create_task, get_task, list_tasks, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["task"])

@router.post("/", response_model=TaskOut, status_code=201)
def create_task_for_user(task_in: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = create_task(db, owner_id=current_user.id, title=task_in.title, description=task_in.description)
    return task

@router.get("/", response_model=List[TaskOut])
def read_task(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return list_tasks(db, current_user.id)

@router.get("/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/task_id", response_model=TaskOut)
def edit_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task(db, task_id, current_user, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = update_task(db , task, title=task_in.title, description=task_in.description, completed=task_in.completed)
    return updated

@router.delete("/{task_id}", status_code=204)
def remove_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, task)
    return None