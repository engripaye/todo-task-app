from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine, Base
from app.models.user import User
from app.models.task import Task

def init_db():
    """Initialize the database tables (only if needed)."""
    Base.metadata.create_all(bind=engine)

def create_user(db: Session, username: str, email: str):
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_task(db: Session, title: str, description: str, user_id: int):
    task = Task(title=title, description=description, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def update_task(db: Session, task_id: int, new_title: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = new_title
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

if __name__ == "__main__":
    db = SessionLocal()

    # Step 1: Create a new user
    user = create_user(db, username="john_doe", email="john@example.com")
    print(f"✅ Created User: {user.username} (id={user.id})")

    # Step 2: Add tasks for this user
    task1 = create_task(db, "Buy groceries", "Milk, Eggs, Bread", user.id)
    task2 = create_task(db, "Finish project", "Complete Alembic migration", user.id)
    print(f"✅ Created Tasks: {task1.title}, {task2.title}")

    # Step 3: Query tasks
    tasks = get_tasks(db, user.id)
    print("\n📋 User's Tasks:")
    for t in tasks:
        print(f"- {t.title}: {t.description}")

    # Step 4: Update a task
    updated = update_task(db, task1.id, "Buy groceries and fruits")
    print(f"\n✏️ Updated Task: {updated.title}")

    # Step 5: Delete a task
    delete_task(db, task2.id)
    print(f"\n🗑️ Deleted Task ID {task2.id}")

    # Final task list
    tasks = get_tasks(db, user.id)
    print("\n📋 Final Tasks:")
    for t in tasks:
        print(f"- {t.title}: {t.description}")

    db.close()
