from flask import Blueprint, jsonify
from ..services.employeeService import EmployeeService
from ..services.managersService import ManagerService
from datetime import datetime
from flask_mail import Message
from ..extensions import mail



class SenderController:

    def __init__(self):
        self.blueprint = Blueprint('sending', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/sendAggregatedEmployeeData', view_func=self.send_aggregated_employee_data, methods=['GET'])
        self.blueprint.add_url_rule('/sendPdfToEmployees', view_func=self.send_pdf_to_employees, methods=['GET'])

    @staticmethod
    def send_aggregated_employee_data():
        recipients = [manager.email for manager in ManagerService.get_all_managers()]

        try:
            msg = Message(
                subject="Monthly Employees Summary Report",
                recipients=recipients,
                body="Hello,\n\nPlease find attached the employees summary report for the last month.\n\nRegards,\nHR Team"
            )
            file_name = "employee_data_" + str(datetime.now().strftime("%B%Y")) + ".xlsx"
            with open("reports/" + file_name, "rb") as f:
                msg.attach(file_name, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                           f.read())

            mail.send(msg)

            return jsonify({"message": "Excel file sent successfully to chief manager."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @staticmethod
    def send_pdf_to_employees():
        employees = EmployeeService.get_all_employees()
        employee = employees[0]

        # for employee in employees:

        try:
            msg = Message(
                subject="Payroll Report – " + str(datetime.now().strftime("%B %Y")),
                recipients=["secrieru.eliza@gmail.com"],
                body="Attached to this email, you will find your salary report for the month of " + str(
                    datetime.now().strftime(
                        "%B%Y")) + ".\nTo open the file, the password is your personal identification number - CNP.\n\nThank you!\nPayroll Team"
            )
            file_name = "employee" + str(employee.id) + "_" + str(datetime.now().strftime("%B%Y")) + ".pdf"
            with open("reports/" + file_name, "rb") as f:
                msg.attach(file_name, "application/pdf", f.read())

            mail.send(msg)

            return jsonify({f"message": f"Pdf file sent successfully to employee {employee.id}"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
