from flask import Flask
from o_evmt.extensions import db
from o_evmt.routes.client import client_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    app.register_blueprint(client_bp)

    return app
