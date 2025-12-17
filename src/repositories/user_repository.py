from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate
from src.utils.security import hash_password

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: UserCreate):
    hashed_pw = hash_password(user_data.password)
    db_user = User(
        email=user_data.email,
        password_hash=hashed_pw,
        role=user_data.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user