from app.schemas.connection import ConnectionBase

class ConnectionService:
    def __init__(self, repository):
        self.repository = repository

    async def create_connection(self, connection: ConnectionBase):
        return await self.repository.create_connection(connection)