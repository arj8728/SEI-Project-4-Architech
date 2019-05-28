from app import app
from controllers import buildings

app.register_blueprint(buildings.router)
