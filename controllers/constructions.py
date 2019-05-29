from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Construction import Construction, ConstructionSchema

router = Blueprint(__name__, 'constructions')

@router.route('/constructions', methods=['GET'])
@db_session
def index():
    schema = ConstructionSchema(many=True)
    constructions = Construction.select()
    return schema.dumps(constructions)

@router.route('/constructions', methods=['POST'])
@db_session
def create():
    schema = ConstructionSchema()

    try:
        data = schema.load(request.get_json())
        construction = Construction(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422
    return schema.dumps(construction), 201

@router.route('/constructions/<int:construction_id>', methods=['GET'])
@db_session
def show(construction_id):
    schema = ConstructionSchema()
    construction = Construction.get(id=construction_id)

    if not construction:
        abort(404)

    return schema.dumps(construction)

@router.route('/constructions/<int:construction_id>', methods=['PUT'])
@db_session
#@secure_route
def update(construction_id):
    schema = ConstructionSchema()
    construction = Construction.get(id=construction_id)


    if not construction:
        abort(404)

    try:
        data = schema.load(request.get_json())
        construction.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(construction)


@router.route('/constructions/<int:construction_id>', methods=['DELETE'])
@db_session
#@secure_route
def delete(construction_id):
    construction = Construction.get(id=construction_id)

    if not construction:
        abort(404)

    construction.delete()
    db.commit()

    return '', 204
