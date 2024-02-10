from fastapi import Depends,APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from database.connection import get_db
from typing import Annotated
from fastapi.security import  OAuth2PasswordBearer, OAuth2PasswordRequestForm
from repository import user_crud
from schema import user_schema
from security.user_security import ALGORITHM, SECRET_KEY, authenticate_user, create_access_token, get_current_user, verify_token,SECRET_KEY
from jose import JWTError, jwt




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user_Router = APIRouter(prefix="/user")



@user_Router.post("/create/", response_model=user_schema.User,tags=["users"])
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)



# Login route
@user_Router.post("/token",tags=["users"])
async def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(User=user)
    return {"access_token": access_token, "token_type": "bearer"}




@user_Router.get("/protected1",tags=["protected"])
async def protected_token(username: str = Depends(verify_token)):
    return {"message": f"Welcome to the protected route, {username}!"}



@user_Router.get("/protected2",tags=["protected"])
async def protected_oauth2_scheme(token: str = Depends(get_current_user)):
    return {"token": token}