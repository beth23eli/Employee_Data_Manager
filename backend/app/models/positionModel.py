from ..extensions import db

class Position(db.Model):
    __tablename__='positions'

    id = db.Column(db.Integer, db.Sequence('positions_id_seq'), primary_key=True)

    title = db.Column(db.String(32), unique=True, nullable=False)

    salary = db.Column(db.Numeric(10, 2), nullable=False)


    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

