
from flask_restplus import Namespace, fields


class SongDTO:
    api = Namespace('song', description='song related operations')
    song = api.model('song', {
        'id': fields.String(required=True, description='song''s identify'),
        'title': fields.String(required=True, description='song''s title'),
        'artist': fields.String(required=True, description='song''s artist'),
        'album': fields.String(required=True, description='song''s album'),
        'year': fields.String(required=True, description='song''s year'),
        'rate': fields.String(required=True, description='song''s rate'),
        'length': fields.String(required=True, description='song''s length'),
        'lyrics': fields.String(required=True, description='song''s lyrics'),
    })
