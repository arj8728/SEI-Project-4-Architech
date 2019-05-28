from flask import Flask
from pony.orm import Database

app = Flask(__name__)
db = Database()
db.bind(provider='postgres', database='building-db')
from models.Building import Building

db.generate_mapping(create_tables=True)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'Hello mate!', 200
