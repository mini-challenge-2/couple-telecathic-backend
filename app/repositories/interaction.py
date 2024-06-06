from app.schemas.interaction import InteractionBase
from app.models.interaction import Interaction

class InteractionRepository:
    def __init__(self, db):
        self.db = db

    async def create_interaction(self, interaction: InteractionBase):
        data = {
            "sender_id": interaction.sender_id,
            "message_id": interaction.message_id,
            "connection_id": interaction.connection_id
        }

        db_interaction = Interaction(**data)
        self.db.add(db_interaction)
        self.db.commit()
        self.db.refresh(db_interaction)
        return db_interaction