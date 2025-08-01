from ..extensions import db, faker
from ..models.managerModel import Manager
from ..models.employeeModel import Employee
from ..models.positionModel import Position
import random

def populate_managers(count=10):
    db.session.add(Manager('Eliza', 'Secrieru', 'secrieru.eliza@gmail.com'))
    # for _ in range(count):
    #     name = faker.first_name()
    #     surname = faker.last_name()
    #     email = faker.email()
    #
    #     db.session.add(Manager(name=name, surname=surname, email=email))

    db.session.commit()

def populate_employees(count=99):
    from ..models.positionModel import Position

    all_positions = Position.query.all()

    db.session.add(
        Employee(
            'Maria', 'Secrieru', 6000000000000, 'maria.secrieru@endava.com',
            position=random.choice(all_positions),
            manager_id=1,
            num_worked_days=19,
            num_vacation_days=1,
            bonuses=0
        )
    )

    for _ in range(count):
        name = faker.first_name()
        surname = faker.last_name()
        email = faker.email()
        cnp_number = faker.random_number(13)
        manager_id = 1
        num_worked_days = random.randint(15, 20)
        num_vacation_days = random.randint(0, 5)
        bonuses = random.randint(0, 300)
        position = random.choice(all_positions)

        db.session.add(Employee(
            name, surname, cnp_number, email,
            position=position,
            manager_id=manager_id,
            num_worked_days=num_worked_days,
            num_vacation_days=num_vacation_days,
            bonuses=bonuses
        ))

    db.session.commit()


def populate_positions():
    positions = [
        ("Junior Developer", 4000),
        ("Software Engineer", 6000),
        ("Full Stack Developer", 5500),
        ("Lead Developer", 10000)
    ]

    for title, salary in positions:
        db.session.add(Position(title=title, salary=salary))

    db.session.commit()