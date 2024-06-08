from app.schemas.interaction import InteractionBase
from app.schemas.interaction import NotificationRequest

class InteractionService:
    def __init__(self, repository):
        self.repository = repository

    async def create_interaction(self, interaction: InteractionBase):
        return await self.repository.create_interaction(interaction)

    async def send_interaction(self, notification: NotificationRequest):
        return await self.repository.send_interaction(notification)