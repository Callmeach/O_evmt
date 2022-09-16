from datetime import date

from flask import Blueprint, request, jsonify, abort

from ..models.domaine import Domaine
from ..models.publication import Publication
from ..models.enterprise import Entreprise

entreprise_bp = Blueprint('entreprise_bp', __name__, url_prefix='/entreprises')


# creation
@entreprise_bp.route('/', methods=['POST'])
def create():
    body = request.get_json()

    nom = body.get('nom', None)
    description = body.get('description', None)

    pays = body.get('pays', None)
    ville = body.get('ville', None)
    mail = body.get('mail', None)
    contact = body.get('contact', None)

    domaine = Domaine.query.filter(Domaine.libelle == body.get('domaine', None)).first()
    abonnement = body.get('abonnement', None)
    abonPub = body.get('abonPub', None)

    print(domaine.id)
    entreprise = Entreprise(nom=nom, description=description, pays=pays, ville=ville, mail=mail,
                            contact=contact, abonnement=abonnement, abonPub=abonPub,
                            idDomaine=domaine.id)  # , domaine_id=domaine.id
    print(entreprise)
    entreprise.insert()

    return jsonify(
        {
            'message': 'Exposant créé avec succes',
            'nom': nom,
            'prenom': description,
            'pays': pays,
            'ville': ville,
            'mail': mail,
            'contact': contact,
            'domaine_id': domaine.id,
            'abonnement': abonnement,
            'abonPub': abonPub
        }
    )


# get all
@entreprise_bp.route('/')
def get_all():
    all = [ent.format() for ent in Entreprise.query.all()]

    return jsonify({
        'success': True,
        'total': len(all),
        'enterprises': all
    })


@entreprise_bp.route('/<int:id>')
def get(id: int):
    ent = Entreprise.exists(id)
    if ent is not False:
        return jsonify({
            'success': True,
            'entreprise': ent.format()
        })
    else:
        abort(404)


@entreprise_bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    ent = Entreprise.exists(id)
    if ent is not False:
        ent.delete()
    else:
        abort(404)


@entreprise_bp.route('/<int:id>', methods=['PATCH'])
def update(id: int):
    ent = Entreprise.exists(id)
    if ent is not False:
        body = request.get_json()

        # Hard Coding
        # TODO : Create a project that will automatically generate CRUD with FLASK
        nom = body.get('nom', None)
        if nom is not None:
            ent.nom = nom
        description = body.get('description', None)
        if description is not None:
            ent.description = description
        pays = body.get('pays', None)
        if pays is not None:
            ent.pays = pays

        ville = body.get('ville', None)
        if ville is not None:
            ent.ville = ville
        mail = body.get('mail', None)
        if mail is not None:
            ent.mail = mail
        contact = body.get('contact', None)
        if contact is not None:
            ent.contact = contact

        domaine = Domaine.query.filter(Domaine.libelle == body.get('domaine', None)).first()
        if domaine is not None:
            ent.domaine_id = domaine.id
        abonnement = body.get('abonnement', None)
        if abonnement is not None:
            ent.abonnement = abonnement
        abonPub = body.get('abonPub', None)
        if abonPub is not None:
            ent.abonPub = abonPub
        ent.update()
    else:
        abort(404)

# TODO : implement search methods
