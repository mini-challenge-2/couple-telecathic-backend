from app.schemas.interaction import InteractionBase
from app.models.interaction import Interaction
from app.schemas.interaction import NotificationRequest
from app.utils.dependency import generate_jwt_token, load_private_key
import requests

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
        db_interaction = db_interaction.__dict__
        del db_interaction['_sa_instance_state']
        return db_interaction

    async def send_interaction(self, notification: NotificationRequest):
        private_key = load_private_key('AuthKey S95F7MWX5R.p8')
        token = generate_jwt_token('S95F7MWX5R', 'DJFUU6576B', private_key)
        url = f"https://api.sandbox.push.apple.com/3/device/{notification.token}"
        headers = {
            "authorization": f"bearer {token}",
            "apns-topic": 'com.liefransim.couple-telecathic',
        }

        payload = {
            "aps": {
                "alert": {
                    "title": notification.title,
                    "body": notification.body
                },
                "sound": "default"
            }
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 500:
            return response
        return 200
