from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserBase
from app.schemas.user import User as UserSchema
from app.models.user import User as UserModel
from app.db import get_db
from app.schemas import Response
from app.utils.dependency import generate_uuid

router = APIRouter()


@router.post('/register')
async def register(user: UserBase, db: Session = Depends(get_db)):
    try:
        pass
        __uuid = generate_uuid()
        if (db.query(UserModel).filter(UserModel.email == user.email).first()) or (db.query(UserModel).filter(UserModel.username == user.username).first()):
            return Response(status=400, message="User already exists")

        data = {
            "id": __uuid,
            "apple_id": user.apple_id,
            "username": user.username,
            "sex": user.sex.name,
            "email": user.email,
            "birth": user.birth,
            "latitude": user.latitude,
            "longitude": user.longitude
        }

        db_user = UserModel(**data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return Response(status=201, message="User created successfully", data=db_user)
    except Exception as e:
        return Response(status=500, message=str(e))