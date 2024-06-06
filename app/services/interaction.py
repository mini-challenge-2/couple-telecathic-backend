from app.schemas.interaction import InteractionBase

class InteractionService:
    def __init__(self, repository):
        self.repository = repository

    async def create_interaction(self, interaction: InteractionBase):
        return await self.repository.create_interaction(interaction)