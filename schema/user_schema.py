from pydantic import BaseModel
from datetime import datetime
from schema.task_schema import Task


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []
    username: str
    created_at: datetime

    class Config:
        orm_mode = True