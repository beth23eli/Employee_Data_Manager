from flask import Blueprint, jsonify
from ..models.employeeModel import Employee

class GeneratorController:
    def __init__(self):
        self.blueprint = Blueprint('generator', __name__)
        self._register_routes()

    def _register_routes(self):
        self.blueprint.add_url_rule("/createAggregatedEmployeeData", view_func=self.createAggregatedEmployeeData, methods=["GET"])


    def createAggregatedEmployeeData(self):
        return jsonify({})
