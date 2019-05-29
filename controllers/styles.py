from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Style import Style, StyleSchema

router = Blueprint(__name__, 'styles')

@router.route('/styles', methods=['GET'])
@db_session
def index():
    schema = StyleSchema(many=True)
    styles = Style.select()
    return schema.dumps(styles)

@router.route('/styles', methods=['POST'])
@db_session
def create():
    schema = StyleSchema()

    try:
        data = schema.load(request.get_json())
        style = Style(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422
    return schema.dumps(style), 201

@router.route('/styles/<int:style_id>', methods=['GET'])
@db_session
def show(style_id):
    schema = StyleSchema()
    style = Style.get(id=style_id)

    if not style:
        abort(404)

    return schema.dumps(style)
