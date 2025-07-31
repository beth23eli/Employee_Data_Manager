from app.models.employeeModel import Employee
from ..extensions import db


class EmployeeService:
    @staticmethod
    def get_all_employees():
        return Employee.query.all()

    @staticmethod
    def get_employee(employee_id):
        return Employee.query.get(employee_id)

    @staticmethod
    def create(data):
        emp = Employee(**data)
        db.session.add(emp)
        db.session.commit()
        return emp

    # @staticmethod
    # def delete_employees():
    #     db.session.query(Employee).delete()
    #     db.session.commit()

