from sqlalchemy.orm import Session

from model import user_model
from schema import user_schema
from security.user_security import hash_password


def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(user_model.User).filter(user_model.User.username == username).first()

def get_user_by_id(db: Session, id: int):
    return db.query(user_model.User).filter(user_model.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    fake_hashed_password = hash_password(user.password)
    db_user = user_model.User(username=user.username,password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


