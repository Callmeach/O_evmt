from o_evmt.extensions import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    lieu = db.Column(db.String(50), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    entreprise_id = db.Column(db.Integer, db.ForeignKey('entreprises.id'))

    def __init__(self, libelle, date, lieu, admin, entreprise):
        self.libelle = libelle,
        self.date = date,
        self.lieu = lieu,
        self.admin_id = admin,
        self.entreprise_id = entreprise

    def event_format(self):
        return {
            'id': self.id,
            'libelle': self.libelle,
            'date': self.date,
            'lieu': self.lieu,
            'admin': self.admin_id,
            'entreprise': self.entreprise_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()