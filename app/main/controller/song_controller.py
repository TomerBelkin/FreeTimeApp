from flask import request
from flask_restplus import Resource

from ..Dal.SongDTO import SongDTO
from ..service.song_service import save_new_song, get_all_songs, get_a_song, download_songs, fill_db, delete_song

api = SongDTO.api
_song = SongDTO.song


@api.route('/')
class SongList(Resource):
    @api.doc('list_of_existing_songs')
    @api.marshal_list_with(_song, envelope='data')
    def get(self):
        """List all exsisting songs"""
        return get_all_songs()

    @api.response(201, 'Song successfully created.')
    @api.doc('create a new song')
    @api.expect(_song, validate=True)
    def post(self):
        """Creates a new song """
        data = request.json
        return save_new_song(data=data)


@api.route('/<id>')
@api.param('id', 'The song identifier')
@api.response(404, 'Song not found.')
class Song(Resource):
    @api.doc('get a song')
    @api.marshal_with(_song)
    def get(self, id):
        """get a song given its identifier"""
        song = get_a_song(id)
        if not song:
            api.abort(404)
        else:
            return song

    def delete(self):
        song = delete_song(id)
        if not song:
            api.abort(404)
        else:
            return song


@api.route('/download')
@api.response(404, 'Song not found.')
class Song(Resource):
    def get(self):
        print("get works")
    def post(self):
        """get a song given its identifier"""
        try:
            songs = request.data.decode('utf-8')
            download_songs(songs)
            print("songs downloaded")
            return ("start_download_songs")
        except Exception as e:
            print(e)

@api.route('/fill-db')
@api.response(404, 'Song not found.')
class Song(Resource):
    def get(self):
        """get a song given its identifier"""
        try:
            fill_db()
            print("songs migrated")
        except Exception as e:
            print(e)



