from o_evmt.extensions import db
from .personne import Personne


class Exposant(Personne):
    __tablename__ = 'exposant'
    id = db.Column(db.Integer, db.ForeignKey("personne.id"), primary_key=True)
    domaine_id = db.Column(db.Integer, db.ForeignKey('domaine.id'))
    specialisation = db.Column(db.String(50), nullable=False)
    abonnement = db.Column(db.String(50), nullable=False)
    abonPub = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "exposant"
    }

    def __init__(self, nom, prenom, dateNaiss, pays, ville, mail, telephone, domaine_id, specialisation, abonnement, abonPub):
        Personne.__init__(self, nom, prenom, dateNaiss, pays, ville, mail, telephone)
        self.domaine_id = domaine_id
        self.specialisation = specialisation
        self.abonnement = abonnement
        self.abonPub = abonPub

    def insert(self):
        db.session.add(self)
        db.session.commit()
