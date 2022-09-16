from flask import Flask
from o_evmt.extensions import db
from o_evmt.routes.client import client_bp
from o_evmt.routes.commentaire import commentaire_bp
from o_evmt.routes.domaine import domaine_bp
from o_evmt.routes.entreprise import entreprise_bp
from o_evmt.routes.exposant import exposant_bp
from o_evmt.routes.publication import publication_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    app.register_blueprint(client_bp)
    app.register_blueprint(domaine_bp)
    app.register_blueprint(exposant_bp)
    app.register_blueprint(commentaire_bp)
    app.register_blueprint(publication_bp)
    app.register_blueprint(entreprise_bp)

    return app
