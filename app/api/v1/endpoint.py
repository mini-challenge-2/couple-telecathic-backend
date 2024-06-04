from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserBase
from app.db import get_db
from app.schemas import Response
import uuid

router = APIRouter()


@router.post('/register')
async def register(user: UserBase, db: Session = Depends(get_db)):
    try:
        pass
        __uuid = str(uuid)
    except Exception as e:
        return Response(status=500, message=str(e))