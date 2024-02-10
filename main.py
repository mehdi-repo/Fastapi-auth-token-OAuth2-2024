import uvicorn
from fastapi import APIRouter, FastAPI

from database.connection import Base,engine
from route import user_route,task_route

# Create the database tables
Base.metadata.create_all(bind=engine)



app = FastAPI()

# config routes
app.include_router(user_route.user_Router)
app.include_router(task_route.task_Router)


@app.get("/")
async def index():
   return {"message": "Hello World"}




if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)