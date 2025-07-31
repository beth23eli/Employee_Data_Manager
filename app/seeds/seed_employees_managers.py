from app.extensions import db, faker
from ..models.managerModel import Manager
from ..models.employeeModel import Employee
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
    positions = {
        "Junior_Developer": 4000,
        "Software_Engineer": 6000,
        "Full Stack Developer": 5500,
        "Lead Developer": 10000,
    }

    db.session.add(
        Employee('Maria', 'Secrieru', 6000000000000, 'maria.secrieru@endava.com', 'Junior Developer', 1, 19, 1, 4000,0))
    for _ in range(count):
        name = faker.first_name()
        surname = faker.last_name()
        email = faker.email()
        cnp_number = faker.random_number(13)
        # manager_id = random.randint(1, 10)
        manager_id = 1
        num_worked_days = random.randint(15, 20)
        num_vacation_days = random.randint(0, 5)
        bonuses = random.randint(0, 300)
        position, salary = random.choice(list(positions.items()))

        db.session.add(Employee(name, surname, cnp_number, email, position, manager_id, num_worked_days, num_vacation_days, salary, bonuses))

    db.session.commit()