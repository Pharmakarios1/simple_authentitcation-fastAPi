from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from ..models import user_model
from ..schemas import user_schema
from ..utils import password_hashed




def create_user(user:user_schema.UserCreate, db: Session ):
    db_user = db.query(user_model.User).filter(user_model.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_pw = password_hashed(user.password)
    new_user = user_model(email=user.email, hashed_password= hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(user: user_schema.UserLogin, db:Session):
     db_user = db.query(user_model.User).filter(user_model.User.email == user.email).first()
     if not db_user or not password_hashed.verify_password(user.password == db_user.hashed_password):
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials")
     
     token = password_hashed.create_access_token({"sub":db_user.email})
     return {"access_token":token, "token_type":"bearer"}