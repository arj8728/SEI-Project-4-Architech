from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

class Building(db.Entity):
    name = Required(str)
    architect = Required(str)
    style = Required(str)
    address = Required(str)
    post_code = Required(str)
    constructions = Set('Construction')
    built = Required(int)
    image = Required(str)

class BuildingSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    architect = fields.Str(required=True)
    style = fields.Str(required=True)
    address = fields.Str(required=True)
    post_code = fields.Str(required=True)
    constructions = fields.Nested('ConstructionSchema', many=True, exclude=('buildings',), dump_only=True)
    built = fields.Int(required=True)
    image = fields.Str(required=True)
