from flask import Blueprint, request, jsonify
from app.services.employeeService import EmployeeService

class EmployeeController:
    def __init__(self):
        self.blueprint = Blueprint('employee', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/<int:employee_id>', view_func=self.get_employee, methods=['GET'])
        self.blueprint.add_url_rule('/create', view_func=self.create_employee, methods=['POST'])
        self.blueprint.add_url_rule('/all', view_func=self.get_all_employees, methods=['GET'])
        #self.blueprint.add_url_rule('/delete', view_func=self.delete_employees, methods=['DELETE'])

    @staticmethod
    def get_employee(employee_id):
        employee = EmployeeService.get_employee(employee_id)

        if not employee:
            return jsonify({'error': 'Employee not found'}), 404
        return jsonify({
            'id': employee.id,
            'manager_id': employee.manager_id,
            'name': employee.name,
            'surname': employee.surname,
            'email': employee.email,
            'salary': employee.salary
        })

    @staticmethod
    def create_employee():
        employee_data = request.get_json()
        employee = EmployeeService.create(employee_data)

        return jsonify({'id': employee.id}), 201

    @staticmethod
    def get_all_employees():
        employees = EmployeeService.get_all_employees()

        return jsonify([
            {
                'id': employee.id,
                'name': employee.name,
                'surname': employee.surname,
                'email': employee.email,
                'manager_id': employee.manager_id
            } for employee in employees
        ])

    # @staticmethod
    # def delete_employees():
    #     EmployeeService.delete_employees()
    #
    #     return jsonify({"All employees deleted"}), 200