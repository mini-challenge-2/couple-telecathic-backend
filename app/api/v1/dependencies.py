from fastapi import Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.repositories.user import UserRepository
from app.services.user import UserService
from app.repositories.connection import ConnectionRepository
from app.services.connection import ConnectionService
from app.repositories.interaction import InteractionRepository
from app.services.interaction import InteractionService

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)

def get_connection_repository(db: Session = Depends(get_db)):
    return ConnectionRepository(db)

def get_connection_service(repository: ConnectionRepository = Depends(get_connection_repository)):
    return ConnectionService(repository)

def get_interaction_repository(db: Session = Depends(get_db)):
    return InteractionRepository(db)

def get_interaction_service(repository: InteractionRepository = Depends(get_interaction_repository)):
    return InteractionService(repository)