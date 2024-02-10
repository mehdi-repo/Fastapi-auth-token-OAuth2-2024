from sqlalchemy import Boolean, Column, Integer, String,DateTime
from datetime import datetime
from database.connection import Base
from sqlalchemy.orm import  relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="user")


