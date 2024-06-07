from app.schemas.user import UserBase

class UserService:
    def __init__(self, repository):
        self.repository = repository

    async def create_user(self, user: UserBase):
        return await self.repository.create_user(user)

    async def register_device(self, user_id: str, token: str):
        return await self.repository.register_device(user_id, token)

    async def get_registered_device(self, user_id: str):
        return await self.repository.get_registered_device(user_id)