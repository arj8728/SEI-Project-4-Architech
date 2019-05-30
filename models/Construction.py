from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

# The model describes the database table
class Construction(db.Entity):
    name = Required(str)
    buildings = Set('Building') # Describes the Many side of a M:M relationship

# The `schema` descibes the serialization/deserialization
class ConstructionSchema(Schema):
    id = fields.Int(dump_only=True) # dump_only means "write only"
    name = fields.Str(required=True)
    buildings = fields.Nested('BuildingSchema', many=True, exclude=('construction',), dump_only=True)
