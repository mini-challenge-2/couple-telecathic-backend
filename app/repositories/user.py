from app.schemas.user import UserBase
from app.utils.dependency import generate_uuid
from app.models.user import User
from app.models.user import UserDevice
from app.schemas import Response

class UserRepository:
    def __init__(self, db):
        self.db = db

    async def create_user(self, user: UserBase):
        __uuid = generate_uuid()
        if (self.db.query(User).filter(User.email == user.email).first()) or (self.db.query(User).filter(User.username == user.username).first()):
            return 400

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

    async def register_device(self, user_id: str, token: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return 404

        data = {
            "user_id": user.id,
            "token": token
        }

        db_device_token = UserDevice(**data)
        self.db.add(db_device_token)
        self.db.commit()
        self.db.refresh(db_device_token)
        db_device_token = db_device_token.__dict__
        del db_device_token['_sa_instance_state']
        return db_device_token

    async def get_registered_device(self, user_id: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        device_token = self.db.query(UserDevice).filter(UserDevice.user_id == user_id).all()
        if not device_token:
            return None

        devices = []
        for device in device_token:
            device = device.__dict__
            del device['_sa_instance_state']
            devices.append(device)

        return devices

    async def get_user(self, apple_id: str):
        user = self.db.query(User).filter(User.apple_id == apple_id).first()
        if not user:
            return None

        user = user.__dict__
        del user['_sa_instance_state']
        return user