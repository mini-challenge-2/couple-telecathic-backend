from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.repositories.user import UserRepository
from app.services.user import UserService

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)