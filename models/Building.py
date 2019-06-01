# import requests
from app import db
from pony.orm import Required, Optional
from marshmallow import Schema, fields, post_load

from .Style import Style
from .Construction import Construction


class Building(db.Entity):
    name = Required(str)
    architect = Required(str)
    style = Required('Style')
    address = Required(str)
    postcode = Required(str)
    construction = Required('Construction')
    built = Required(int)
    image = Required(str)
    user = Required('User')
    latitude = Required(float)
    longitude = Required(float)
    about = Optional(str)

class BuildingSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    architect = fields.Str(required=True)
    style = fields.Nested('StyleSchema', exclude=('buildings',), dump_only=True)
    style_id = fields.Int(load_only=True)
    address = fields.Str(required=True)
    postcode = fields.Str(required=True)
    construction = fields.Nested('ConstructionSchema', exclude=('buildings',), dump_only=True)
    construction_id = fields.Int(load_only=True)
    built = fields.Int(required=True)
    image = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('email', 'buildings'))
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    about = fields.Str()

    @post_load
    def load_style(self, data):
        data['style'] = Style.get(id=data['style_id'])
        del data['style_id']

        return data

    @post_load
    def load_construction(self, data):
        data['construction'] = Construction.get(id=data['construction_id'])
        del data['construction_id']

        return data


    # @post_load
    # def load_construction(self, data):
    #     data['construction'] = [Construction.get(id=cont_id) for cont_id in data['construction_id']]
    #     del data['construction_id']
    #
    #     return data



# change the construction to be the same as styles so that in the Building it will change to constructions = Required('Constructions')
# in the building schema the contructions  should follow the same format as the styles get rid of the many = true
