from o_evmt.extensions import db


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exposant_id = db.Column(db.Integer, db.ForeignKey('exposant.id'))
    coordonnees = db.Column(db.String(50), nullable=False)
    lienPhoto = db.Column(db.String(50))
    lienVideo = db.Column(db.String(50))
