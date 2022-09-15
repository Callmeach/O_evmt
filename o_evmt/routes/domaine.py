from flask import Blueprint, request, jsonify, abort
from ..models.domaine import Domaine

domaine_bp = Blueprint("domaine_bp", __name__, url_prefix='/domaine')


# @domaine_bp.post('/create')
# def create():
#     body = request.get_json()
#     libelle = body.get('libelle', None)
#     domaine = Domaine(libelle=libelle)
#     domaine.insert()
#
#     return jsonify(
#         {
#             'message': 'Domaine crée avec succes',
#             'libelle': libelle
#         }
#     )
