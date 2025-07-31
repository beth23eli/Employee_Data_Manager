from flask import Blueprint, request, jsonify
from app.services.employeeService import EmployeeService
from .generationController import GeneratorController as gc
from .sendingController import SenderController as sc


class EmployeeController:

    def __init__(self):
        self.blueprint = Blueprint('employees', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/<int:employee_id>', view_func=self.get_employee, methods=['GET'])
        self.blueprint.add_url_rule('/create', view_func=self.create_employee, methods=['POST'])
        self.blueprint.add_url_rule('/all', view_func=self.get_all_employees, methods=['GET'])


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

    @staticmethod
    def do_monthly_report():

        try:
            print("Doing monthly reporting...")
            try:
                print("Generating...")
                gc.create_aggregated_employee_data()
                gc.create_pdf_for_employees()
            except Exception as e:
                return jsonify({"error": f"Generation failed: {str(e)}"}), 400

            try:
                print("Sending...")
                sc.send_aggregated_employee_data()
                sc.send_pdf_to_employees()
            except Exception as e:
                return jsonify({"error": f"Sending failed: {str(e)}"}), 400

            print("Generating the archive...")
            #aici voi apela functia ce fc arhiva !!!!!!!!!
        except Exception as e:
            return jsonify({"error": f"Monthly reporting failed: {str(e)}"}), 400
