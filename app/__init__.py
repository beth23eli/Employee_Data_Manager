from flask import Flask
from .extensions import db, mail
from .controllers.Generator import GeneratorController
from .controllers.Sender import SenderController
from .controllers.employeeController import EmployeeController
from .models.managerModel import Manager
from .models.employeeModel import Employee
from .seeds.seed_employees_managers import populate_managers, populate_employees
from flask_mail import Mail, Message

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()
        if not db.session.query(db.exists().where(Manager.id == 1)).scalar():
            populate_managers()

        if not db.session.query(db.exists().where(Employee.id == 1)).scalar():
            populate_employees()


    employee_controller = EmployeeController()
    app.register_blueprint(employee_controller.blueprint, url_prefix='/employee')

    return app