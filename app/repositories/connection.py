from app.schemas.connection import ConnectionBase
from app.models.user import User as UserModel
from app.models.connection import Connection
from app.schemas import Response

class ConnectionRepository:
    def __init__(self, db):
        self.db = db

    async def create_connection(self, connection: ConnectionBase):
        user = self.db.query(UserModel).filter(UserModel.id == connection.user_id).first()
        partner = self.db.query(UserModel).filter(UserModel.id == connection.partner_id).first()

        if not user or not partner:
            return Response(status=404, message="User not found")

        data = {
            "user_id": user.id,
            "partner_id": partner.id,
        }

        db_connection = Connection(**data)
        self.db.add(db_connection)
        self.db.commit()
        self.db.refresh(db_connection)
        return Response(status=200, message="Connected successfully")