from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ This is what was missing
Base = declarative_base()
