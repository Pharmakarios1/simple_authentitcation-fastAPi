from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.db import get_db

from ..schemas import user_schema
from ..services import auth_service



router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/signup", response_model=user_schema.UserResponse)
def signup(user: user_schema.UserCreate, db: Session= Depends(get_db)):
    return auth_service.create_user(user, db)


@router.post("/signin", response_model=user_schema.Token)
def signup(user: user_schema.UserLogin, db: Session= Depends(get_db)):
    return auth_service.create_user(user, db)
