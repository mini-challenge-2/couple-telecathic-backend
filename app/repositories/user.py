from app.schemas.user import UserBase
from app.schemas.user import UserDevice
from app.utils.dependency import generate_uuid
from app.models.user import User
from app.schemas import Response

class UserRepository:
    def __init__(self, db):
        self.db = db

    async def create_user(self, user: UserBase):
        __uuid = generate_uuid()
        if (self.db.query(User).filter(User.email == user.email).first()) or (self.db.query(User).filter(User.username == user.username).first()):
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

        db_user = User(**data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        db_user = db_user.__dict__
        del db_user['_sa_instance_state']
        return db_user

    async def register_device(self, user: UserDevice):
        user = self.db.query(User).filter(User.id == user.user_id).first()
        if not user:
            return Response(status=404, message="User not found")

        user.device_token = user.device_token
        self.db.commit()
        # return 