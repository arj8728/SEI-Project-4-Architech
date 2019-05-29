from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields, post_load

from .Style import Style
from .Construction import Construction


class Building(db.Entity):
    name = Required(str)
    architect = Required(str)
    style = Required('Style')
    address = Required(str)
    post_code = Required(str)
    constructions = Set('Construction')
    built = Required(int)
    image = Required(str)


class BuildingSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    architect = fields.Str(required=True)
    style = fields.Nested('StyleSchema', exclude=('buildings',), dump_only=True)
    style_id = fields.Int(load_only=True)
    address = fields.Str(required=True)
    post_code = fields.Str(required=True)
    constructions = fields.Nested('ConstructionSchema', many=True, exclude=('buildings',), dump_only=True)
    construction_ids = fields.List(fields.Int(), load_only=True)
    built = fields.Int(required=True)
    image = fields.Str(required=True)

    @post_load
    def load_style(self, data):
        data['style'] = Style.get(id=data['style_id'])
        del data['style_id']

        return data

    @post_load
    def load_constructions(self, data):
        data['constructions'] = [Construction.get(id=cat_id) for cat_id in data['construction_ids']]
        del data['construction_ids']

        return data
