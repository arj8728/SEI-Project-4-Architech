from app import db
from pony.orm import Required

class Building(db.Entity):
    name = Required(str)
    architect = Required(str)
    style = Required(str)
    address = Required(str)
    post_code = Required(str)
    construction = Required(str)
