from flask import Blueprint, request, jsonify, abort
from datetime import date
from ..models.exposant import Exposant
from ..models.domaine import Domaine

exposant_bp = Blueprint("exposant_bp", __name__, url_prefix='/exposant')


@exposant_bp.post('/create')
def create():
    body = request.get_json()

    nom = body.get('nom', None)
    prenom = body.get('prenom', None)
    dateNaiss = date.today()
    pays = body.get('pays', None)
    ville = body.get('ville', None)
    mail = body.get('mail', None)
    telephone = body.get('telephone', None)

    domaine = Domaine.query.filter(Domaine.libelle == body.get('domaine', None)).first()
    specialisation = body.get('specialisation', None)
    abonnement = body.get('abonnement', None)
    abonPub = body.get('abonPub', None)

    exposant = Exposant(nom=nom, prenom=prenom, dateNaiss=dateNaiss, pays=pays, ville=ville, mail=mail,
                        telephone=telephone, specialisation=specialisation,
                        abonnement=abonnement, abonPub=abonPub, domaine_id=domaine.id)

    exposant.insert()

    return jsonify(
        {
            'message': 'Exposant crée avec succes',
            'nom': nom,
            'prenom': prenom,
            'dateNaiss': dateNaiss,
            'pays': pays,
            'ville': ville,
            'mail': mail,
            'telephone': telephone,
            'domaine_id': domaine.id,
            'specialisation': specialisation,
            'abonnement': abonnement,
            'abonPub': abonPub
        }
    )
