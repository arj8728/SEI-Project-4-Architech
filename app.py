from flask import Flask
from pony.orm import Database

app = Flask(__name__)
db = Database()
db.bind(provider='postgres', database='building-db')

# pylint: disable=W0611, C0413
from config import routes

from models.Building import Building, BuildingSchema


db.generate_mapping(create_tables=True)
