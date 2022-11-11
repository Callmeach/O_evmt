from flask import Blueprint, request, jsonify, abort

from ..models.evenement import Event

event_bp = Blueprint("event_bp", __name__, url_prefix="/event")


@event_bp.get('/')
def get():
    events = [event.event_format() for event in Event.query.all()]

    return jsonify(
        {
            'events': events,
            'total': len(events)
        }
    )


@event_bp.post('/create')
def create():
    body = request.get_json()

    libelle = body.get('libelle', None)
    date = body.get('date', None)
    lieu = body.get('lieu', None)
    admin_id = body.get('admin_id', None)
    entreprise_id = body.get('entreprise_id', None)

    event = Event(libelle=libelle, date=date, lieu=lieu, admin=admin_id, entreprise=entreprise_id)

    event.insert()

    return jsonify(
        {
            'evenement': event.event_format()
        }
    )


@event_bp.patch("/<int:id>")
def update(id):
    event = Event.query.get(id)
    if event is None:
        abort(404)
    else:
        try:
            body = request.get_json()
            event.libelle = body.get('libelle')
            event.date = body.get('date')
            event.lieu = body.get('lieu')

            event.update()

            return jsonify(
                {
                    'event': event.event_format()
                }
            )
        except:
            abort(406)


@event_bp.delete("/<int:id>")
def delete(id):
    event = Event.query.get(id)
    if event is None:
        abort(404)
    else:
        event.delete()
        return {
            'message': 'Evenement supprimé avec succès'
        }
