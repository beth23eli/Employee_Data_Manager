from flask import Blueprint, request, jsonify
from ..services.positionService import PositionService


class PositionController:

    def __init__(self):
        self.blueprint = Blueprint('positions', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/<int:position_id>', view_func=self.get_position, methods=['GET'])
        self.blueprint.add_url_rule('/create', view_func=self.create_position, methods=['POST'])
        self.blueprint.add_url_rule('/all', view_func=self.get_all_positions, methods=['GET'])


    @staticmethod
    def get_position(pos_id):
        position = PositionService.get_position(pos_id)

        if not position:
            return jsonify({'error': 'Position not found'}), 404
        return jsonify({
            'id': position.id,
            'title': position.title,
            'salary': position.salary
        })

    @staticmethod
    def create_position():
        position_data = request.get_json()
        position = PositionService.create(position_data)

        return jsonify({'id': position.id}), 201

    @staticmethod
    def get_all_positions():
        positions = PositionService.get_all_positions()

        return jsonify([
            {
                'id': position.id,
                'title': position.title,
                'salary': position.salary,
            } for position in positions
        ])
