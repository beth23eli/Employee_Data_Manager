from app.models.managerModel import Manager
from ..extensions import db


class ManagerService:
    @staticmethod
    def get_all_managers():
        return Manager.query.all()

    @staticmethod
    def get_manager(manager_id):
        return Manager.query.get(manager_id)

    @staticmethod
    def create(data):
        emp = Manager(**data)
        db.session.add(emp)
        db.session.commit()
        return emp


