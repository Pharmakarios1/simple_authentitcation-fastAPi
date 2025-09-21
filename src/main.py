from fastapi import FastAPI

from .models import user_model
from .db.db import engine
from .routes import auth_routes 
from .utils.env_loader import load_env_file

load_env_file()

app = FastAPI()

user_model.Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)


# @app.get("/")
# async def home():
#     return {"message": "welcome to my first FastAPI course"}

