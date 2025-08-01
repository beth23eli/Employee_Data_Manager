from ..models.positionModel import Position
from ..extensions import db


class PositionService:
    @staticmethod
    def get_all_positions():
        return Position.query.all()

    @staticmethod
    def get_position(position_id):
        return Position.query.get(position_id)

    @staticmethod
    def create(data):
        pos = Position(**data)

        db.session.add(pos)
        db.session.commit()
        return pos

