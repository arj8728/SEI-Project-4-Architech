from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Building import Building, BuildingSchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'buildings')

@router.route('/buildings', methods=['GET'])
@db_session
def index():
    schema = BuildingSchema(many=True)
    buildings = Building.select()
    return schema.dumps(buildings)

@router.route('/buildings', methods=['POST'])
@db_session
@secure_route
def create():
    schema = BuildingSchema()

    try:
        data = schema.load(request.get_json())
        building = Building(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422
    return schema.dumps(building), 201

@router.route('/buildings/<int:building_id>', methods=['GET'])
@db_session
def show(building_id):
    schema = BuildingSchema()
    building = Building.get(id=building_id)

    if not building:
        abort(404)

    return schema.dumps(building)

@router.route('/buildings/<int:building_id>', methods=['PUT'])
@db_session
@secure_route
def update(building_id):
    schema = BuildingSchema()
    building = Building.get(id=building_id)


    if not building:
        abort(404)

    try:
        data = schema.load(request.get_json())
        building.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(building)


@router.route('/buildings/<int:building_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(building_id):
    building = Building.get(id=building_id)

    if not building:
        abort(404)

    building.delete()
    db.commit()

    return '', 204
