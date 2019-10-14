from .. import db
import json

class Song(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    album = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    rate = db.Column(db.Float,)
    length = db.Column(db.String)
    lyrics = db.Column(db.String)



    def set_lyrics(self, lyrics: str):
        self.lyrics = lyrics

    def set_rate(self, rate: int):
        self.rate = rate

    def set_length(self, length: int):
        self.length = length

    def rate_up(self):
        if float(self.rate) <= 9.9:
            self.rate = float(self.rate) + 0.1

    def rate_down(self):
        if float(self.rate) >= 7.1:
            self.rate -= 0.1

    def song_to_json(self):
        return json.dumps(self.__dict__)


#if __name__ == '__main__':
    #s = Song("Creep", "Radiohead", "karma-police", 1997)
    #print(s.song_to_json())