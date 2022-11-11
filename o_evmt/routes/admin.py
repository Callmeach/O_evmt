from flask import Blueprint, request, jsonify, abort

from ..models.admin import Admin

admin_bp = Blueprint("admin_bp", __name__, url_prefix="/admin")


@admin_bp.get('/<int:id>')
def get(id):
    admin = Admin.query.get(id)
    if admin is None:
        abort(404)
    else:
        return jsonify(
            {
                "admin": admin.admin_format()
            }
        )


@admin_bp.post('/create')
def create():
    body = request.get_json()

    nom = body.get('nom', None)

    admin = Admin(nom=nom)

    admin.insert()

    return jsonify(
        {
            'admin': admin.admin_format()
        }
    )


@admin_bp.patch("/<int:id>")
def update(id):
    admin = Admin.query.get(id)
    if admin is None:
        abort(404)
    else:
        try:
            body = request.get_json()
            admin.nom = body.get('nom')
            admin.update()

            return jsonify(
                {
                    'admin': admin.admin_format()
                }
            )
        except:
            abort(406)


@admin_bp.delete("/<int:id>")
def delete(id):
    admin = Admin.query.get(id)
    if admin is None:
        abort(404)
    else:
        admin.delete()
        return {
            'message': 'Administrateur supprimé avec succès'
        }
