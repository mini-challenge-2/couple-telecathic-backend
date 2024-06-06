from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserBase
from app.schemas.connection import ConnectionBase
from app.models.connection import Connection
from app.db import get_db
from app.schemas import Response
from app.schemas.special_day import SpecialDayBase
from app.models.special_day import SpecialDay
from app.services.user import UserService
from app.services.connection import ConnectionService
from .dependencies import get_user_service
from .dependencies import get_connection_service

router = APIRouter()


@router.post('/register')
async def create_user(user: UserBase, service: UserService = Depends(get_user_service)):
    try:
        user = await service.create_user(user)
        return Response(status=201, message="User created successfully", value=user)
    except Exception as e:
        return Response(status=500, message=str(e))

@router.post('/connect')
async def connect(connection: ConnectionBase, service: ConnectionService = Depends(get_connection_service)):
    try:
        return await service.create_connection(connection)
    except Exception as e:
        return Response(status=500, message=str(e))

@router.get('/couple-data/{user_id}')
async def get_couple_data(user_id: str, service: ConnectionService = Depends(get_connection_service)):
    try:
        couple = await service.get_couple_data(user_id)
        return Response(status=200, message="Couple data retrieved successfully", value=couple)
    except Exception as e:
        return Response(status=500, message=str(e))

@router.post('/special-days/{user_id}')
async def add_special_days(user_id: str, special_day: SpecialDayBase, db: Session = Depends(get_db)):
    try:
        connection = db.query(Connection).filter(Connection.user_id == user_id).first()
        if not connection:
            return Response(status=404, message="Connection not found")
        
        data = {
            'connection_id': connection.id,
            'date': special_day.date,
            'description': special_day.description,
            'type': special_day.type.name,
            'color': special_day.color
        }

        db_special_day = SpecialDay(**data)
        db.add(db_special_day)
        db.commit()
        db.refresh(db_special_day)
        return Response(status=201, message="Special day added successfully", data=db_special_day)
    except Exception as e:
        return Response(status=500, message=str(e))