from fastapi import Depends,APIRouter,HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db

from repository import task_crud,user_crud
from schema import task_schema



task_Router = APIRouter(prefix="/task")



@task_Router.post("/create/", response_model=task_schema.Task,tags=["tasks"], summary="Create Task")
def create_user(
    user_id: int, item: task_schema.TaskCreate, db: Session = Depends(get_db)):
    id_user = user_crud.get_user_by_id(db, id=user_id)
    if not id_user:
        raise HTTPException(status_code=400, detail="user is not exist")

    return task_crud.create_user_task(db=db, item=item, user_id=user_id)


