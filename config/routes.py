import os
from flask import abort
from app import app
from controllers import buildings, constructions, styles, auth

app.register_blueprint(buildings.router)
app.register_blueprint(constructions.router)
app.register_blueprint(styles.router)
app.register_blueprint(auth.router)

@app.route('/')
@app.route('/<path:path>')
def catch_all(path='index.html'):
    if os.path.isfile('public/' + path):
        return app.send_static_file(path)

    return abort(404)
