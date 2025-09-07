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


@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="incorrect username or password")
    token = create_access_token(str(user.id))
    return {"access_token": token, "token_type": "bearer"}