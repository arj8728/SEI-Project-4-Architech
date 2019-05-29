from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

# The model describes the database table
class Style(db.Entity):
    name = Required(str)
    buildings = Set('Building') # Describes the Many side of a 1:M reationship

# The `schema` descibes the serialization/deserialization
class StyleSchema(Schema):
    id = fields.Int() # dump_only means "write only"
    name = fields.Str(required=True)
    buildings = fields.Nested('BuildingSchema', many=True, exclude=('style', 'constructions'))
