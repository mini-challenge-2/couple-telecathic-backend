from app.schemas.user import UserBase

class UserService:
    def __init__(self, repository):
        self.repository = repository

    async def create_user(self, user: UserBase):
        return await self.repository.create_user(user)