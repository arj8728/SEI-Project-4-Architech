from app import app
from controllers import buildings, constructions

app.register_blueprint(buildings.router)
app.register_blueprint(constructions.router)
