from app.schemas.connection import ConnectionBase

class ConnectionService:
    def __init__(self, repository):
        self.repository = repository

    async def create_connection(self, connection: ConnectionBase):
        return await self.repository.create_connection(connection)

    async def get_couple_data(self, user_id: str):
        return await self.repository.get_couple_data(user_id)

    async def get_connection(self, user_id: str):
        return await self.repository.get_connection(user_id)