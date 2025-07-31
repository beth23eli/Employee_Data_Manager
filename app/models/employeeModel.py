from sqlalchemy import ForeignKey

from ..extensions import db

class Employee(db.Model):
    __tablename__='employees'

    id = db.Column(db.Integer, db.Sequence('employees_id_seq'), primary_key=True)

    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)

    cnp_number = db.Column(db.String(13), nullable=False)

    email = db.Column(db.String(32), nullable=False)

    position = db.Column(db.String(32), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now(),
                             onupdate=db.func.now())

    manager_id = db.Column(db.Integer, ForeignKey("managers.id", ondelete="CASCADE"), nullable=False)

    num_worked_days = db.Column(db.Integer, nullable=False)

    num_vacation_days = db.Column(db.Integer, nullable=True)

    salary = db.Column(db.Float, nullable=False)

    bonuses = db.Column(db.Float, nullable=True)


    def __init__(self, name, surname, cnp_number, email, position, manager_id, num_worked_days, num_vacation_days, salary, bonuses):
        self.name = name
        self.surname = surname
        self.cnp_number = cnp_number
        self.email = email
        self.position = position
        self.manager_id = manager_id
        self.num_worked_days = num_worked_days
        self.num_vacation_days = num_vacation_days
        self.salary = salary
        self.bonuses = bonuses
