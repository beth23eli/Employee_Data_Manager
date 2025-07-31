from ..extensions import db

class Manager(db.Model):
    __tablename__='managers'

    id = db. Column(db.Integer, db.Sequence('managers_id_seq'), primary_key=True)

    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email