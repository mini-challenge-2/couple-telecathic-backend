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
        db_connection = db_connection.__dict__
        del db_connection['_sa_instance_state']
        return db_connection

    async def get_couple_data(self, user_id: str):
        couple = self.db.query(Connection).filter(Connection.user_id == user_id).first()
        if not couple:
            return Response(status=404, message="Couple not found")

        partner = self.db.query(UserModel).filter(UserModel.id == couple.partner_id).first()
        partner = partner.__dict__
        del partner['_sa_instance_state']
        return partner

    async def get_connection(self, user_id: str):
        connection = self.db.query(Connection).filter(Connection.user_id == user_id).first()
        if not connection:
            return Response(status=404, message="Connection not found")

        connection = connection.__dict__
        del connection['_sa_instance_state']
        return connection