from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.repositories import user_repository
from src.schemas.user import UserCreate, UserLogin
from src.utils.security import verify_password, create_access_token

def register(db: Session, user_data: UserCreate):
    if user_repository.get_user_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_repository.create_user(db, user_data)

def login(db: Session, login_data: UserLogin):
    user = user_repository.get_user_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"user_id": user.id, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}