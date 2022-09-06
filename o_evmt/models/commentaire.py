from .personne import db


class Commentaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
    texteCom = db.Column(db.String(500), nullable=False)
    lienPhoto = db.Column(db.String(255), nullable=False)
