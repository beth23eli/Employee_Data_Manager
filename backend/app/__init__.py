from flask import Flask
from .extensions import db, mail
from .controllers.generationController import GeneratorController
from .controllers.sendingController import SenderController
from .controllers.employeeController import EmployeeController
from .controllers.positionController import PositionController
from .models.managerModel import Manager
from .models.employeeModel import Employee
from .models.positionModel import Position
from .seeds.seed_employees_managers import populate_managers, populate_employees, populate_positions
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()
        if not db.session.query(db.exists().where(Position.id == 1)).scalar():
            populate_positions()

        if not db.session.query(db.exists().where(Manager.id == 1)).scalar():
            populate_managers()

        if not db.session.query(db.exists().where(Employee.id == 1)).scalar():
            populate_employees()


    position_controller = PositionController()
    app.register_blueprint(position_controller.blueprint, url_prefix='/employees/positions')

    employee_controller = EmployeeController()
    app.register_blueprint(employee_controller.blueprint, url_prefix='/employees')

    generation_controller = GeneratorController()
    app.register_blueprint(generation_controller.blueprint, url_prefix='/employees/operations/generation')

    sending_controller = SenderController()
    app.register_blueprint(sending_controller.blueprint, url_prefix='/employees/operations/sending')


    return app