from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token
from app.db.session import SessionLocal
from app.api.dependencies import get_db
from app.crud.user import get_user_by_email, create_user
from app.security import verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut, status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email Already Registered")
    user = create_user(db, user_in.email, user_in.password)
    return user
