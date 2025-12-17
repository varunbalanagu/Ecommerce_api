from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.user import UserCreate, UserLogin, UserResponse
from src.services import user_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_service.register(db, user_data)

@router.post("/login")
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    return user_service.login(db, login_data)