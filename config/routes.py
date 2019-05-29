from app import app
from controllers import buildings, constructions, styles

app.register_blueprint(buildings.router)
app.register_blueprint(constructions.router)
app.register_blueprint(styles.router)
