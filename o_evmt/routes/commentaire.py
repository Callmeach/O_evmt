from flask import Blueprint, request, jsonify, abort

from ..models.commentaire import Commentaire

commentaire_bp = Blueprint("commentaire_bp", __name__, url_prefix="/commentaire")


@commentaire_bp.post('/create')
def create():
    body = request.get_json()

    texteCom = body.get('texteCom', None)
    lienPhoto = body.get('lienPhoto', None)
    client_id = body.get('client_id', None)
    exposant_id = body.get('exposant_id', None)
    publication_id = body.get('publication_id', None)

    commentaire = Commentaire(client=client_id, exposant=exposant_id, publication=publication_id, commentaire=texteCom, photo=lienPhoto)

    commentaire.insert()

    return jsonify(
        {
            'commentaire': commentaire.commentaire_format()
        }
    )


@commentaire_bp.patch("/<int:id>/update")
def update(id):
    commentaire = Commentaire.query.get(id)
    if commentaire is None:
        abort(404)
    else:
        try:
            body = request.get_json()
            commentaire.texteCom = body.get('texteCom')
            commentaire.lienPhoto = body.get('lienPhoto')
            commentaire.update()

            return jsonify(
                {
                    'commentaire': commentaire.commentaire_format()
                }
            )
        except:
            abort(406)


@commentaire_bp.delete("/<int:id>/delete")
def delete(id):
    commentaire = Commentaire.query.get(id)
    if commentaire is None:
        abort(404)
    else:
        commentaire.delete()
        return {
            'message': 'Commentaire supprimé avec succès'
        }
