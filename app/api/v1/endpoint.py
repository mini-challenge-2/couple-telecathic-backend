from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserBase
from app.schemas.connection import ConnectionBase
from app.models.user import User as UserModel
from app.models.connection import Connection
from app.db import get_db
from app.schemas import Response
from app.utils.dependency import generate_uuid
from app.schemas.special_day import SpecialDayBase
from app.models.special_day import SpecialDay
from app.services.user import UserService
from .dependencies import get_user_service

router = APIRouter()


@router.post('/register')
async def create_user(user: UserBase, service: UserService = Depends(get_user_service)):
    try:
        return await service.create_user(user)
    except Exception as e:
        return Response(status=500, message=str(e))

@router.post('/connect')
async def connect(connection: ConnectionBase, db: Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.id == connection.user_id).first()
        partner = db.query(UserModel).filter(UserModel.id == connection.partner_id).first()

        if not user or not partner:
            return Response(status=404, message="User not found")

        data = {
            "user_id": user.id,
            "partner_id": partner.id,
        }

        db_connection = Connection(**data)
        db.add(db_connection)
        db.commit()
        db.refresh(db_connection)
        return Response(status=200, message="Connected successfully")
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