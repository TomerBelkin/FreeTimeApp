import os
import json
from app.main.models import Song
from ..utils import mp3_Handler

class SongDAO(object):
    def __init__(self):
        self.source_directory = "D:\\Tomer\\Music metadata"

    def get_songs_by_album(self, album: str):
        """

        :param album:
        :return:
        """
        try:
            return self.get_all_by_key('Album', album)
        except Exception  as e:
            print(e)

    def get_songs_by_artist(self, artist: str):
        """

        :param artist:
        :return:
        """
        try:
            return self.get_all_by_key('Artist', artist)
        except Exception as e:
            print(e)


    def get_songs_by_year(self, year : int):
        """

        :param year:
        :return:
        """
        try:
            return self.get_all_by_key('Year', year)
        except Exception as e:
            print(e)

    def get_songs_by_rate(self, min_rate: float, max_rate : float):
        """

        :param min_rate:
        :param max_rate:
        :return:
        """
        try:
            return self.get_all_between('Rate',min_rate, max_rate)
        except Exception as e:
            print(e)

    def get_songs_by_length(self, min_length: float, max_length : float):
        """

        :param min_length:
        :param max_length:
        :return:
        """
        try:
            return self.get_all_between('Length', min_length, max_length)
        except Exception as e:
            print(e)

    def get_all_by_key(self, key: str, value: str):
        """
        :param key:
        :param value:
        :return:
        """
        songs = []
        for root, die, files in os.walk(self.source_directory):
            for name in files:
                if name.endswith(".json"):
                    try:
                        with open(self.source_directory + "\\" + name, "r") as read_file:
                            current_song = json.load(read_file)
                            if current_song[key] == value:
                                songs.append(Song.Song(current_song["Title"],
                                                       current_song["Artist"],
                                                       current_song["Album"],
                                                       current_song["Year"],
                                                       current_song["Rate"],
                                                       current_song["Length"],
                                                       current_song["Lyrics"]))
                    except Exception as e:
                        print(name)
        return songs

    def get_all_between(self, key: str, min_val: float, max_val: float):
        """

        :param key:
        :param min_rate:
        :param max_rate:
        :return:
        """
        songs = []
        for root, die, files in os.walk(self.source_directory):
            for name in files:
                if name.endswith(".json"):
                    try:
                        with open(self.source_directory + "\\" + name, "r") as read_file:
                            current_song = json.load(read_file)
                            if (float(current_song[key]) <= max_val) & (float(current_song['Rate']) >= min_val):
                                songs.append(Song.Song(current_song["Title"],
                                                       current_song["Artist"],
                                                       current_song["Album"],
                                                       current_song["Year"],
                                                       current_song["Rate"],
                                                       current_song["Length"],
                                                       current_song["Lyrics"]))
                    except Exception as e:
                        print(e)
        return songs

if __name__ == '__main__':
    mp3_Handler.download_songs_from_file("D:\\Tomer\\Learn\\python\\app\\main\\Dal\\songs_for_download.txt")
    #s = SongDAO()
    #songs_of_dream = s.get_songs_by_artist("Avenged Sevenfold")
    #for song in songs_of_dream:
        #print(song.song_name)
    #print(len(songs_of_dream))
