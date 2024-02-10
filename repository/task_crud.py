from sqlalchemy.orm import Session

from model import task_model
from schema import task_schema



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(task_model.Task).offset(skip).limit(limit).all()


def create_user_task(db: Session, item: task_schema.TaskCreate, user_id: int):
    db_item = task_model.Task(**item.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item