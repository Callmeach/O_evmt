from o_evmt.extensions import db


class Domaine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
