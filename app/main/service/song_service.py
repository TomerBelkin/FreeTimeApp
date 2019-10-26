import datetime
import json
import os

from app.main import db
from app.main.models.Song import Song
from ..utils import mp3_Handler

def save_new_song(data):
    exist = False
    songs = Song.query.filter_by(title=data["Title"])
    for song in songs:
        if song.artist == data["Artist"]:
            exist = True

    if not exist:
        new_song = Song(
            id=get_last_id() + 1,
            title=data["Title"],
            artist=data["Artist"],
            album=data["Album"],
            year=data["Year"],
            rate=data["Rate"],
            length=data["Length"],
            lyrics=data["Lyrics"]
        )
        save_changes(new_song)
        print(new_song.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Song already exists',
        }
        return response_object, 409


def get_all_songs():
    return Song.query.all()

def get_last_id():
    return len(get_all_songs())

def delete_song(id):
    db.session.delete(get_a_song(id))

def get_a_song(id):
    return Song.query.get(id)

def song_exist(data):
    return True

def download_songs():
    print("Downloads began at: " + datetime.datetime.now().strftime("%H:%M:%S"))

    with open("D:\\Tomer\\Learn\\python\\app\\main\\Dal\\songs_for_download.txt") as download_songs_file:
        content = download_songs_file.readlines()
        content = [x.strip() for x in content]
        for wanted_song in content:
            try:
                artist, song_name = wanted_song.split(' - ')
                current_song = mp3_Handler.download_song(artist, song_name)
                current_song["Year"] = 0
                save_new_song(current_song)
            except Exception as e:
                print(e)

    print("Downloads ended at: " + datetime.datetime.now().strftime("%H:%M:%S"))


def order_songs():
    all_songs = get_all_songs()
    fix_id_count = 1
    for song in all_songs:
        song.id = fix_id_count
        fix_id_count +=1
        save_changes(song)
        print(song.artist + " - " + song.title + "-" + str(song.id))

def fill_db():
    """

    :return:
    """
    directory = "D:\\Tomer\\music-check\\"
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".mp3"):
                current_song = mp3_Handler.mp3_to_json("",directory + name)
                current_song["Year"] = 0
                save_new_song(current_song)



def save_changes(data):
    db.session.add(data)
    db.session.commit()
