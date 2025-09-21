from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os


DATABASE_URL ="sqlite:///./auth.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, class_=Session, autoflush=False, autocommit=False )
Base = declarative_base()


#Dependency
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
