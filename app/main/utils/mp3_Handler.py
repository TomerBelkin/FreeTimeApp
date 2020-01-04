from __future__ import unicode_literals
import os
import datetime
import json
import shutil

from lyricwikia import lyricwikia
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from youtube_dl import YoutubeDL
import urllib.request
import urllib.parse
import re

mp3_end = '.mp3'
dal_directory = "D:\\Tomer\\Learn\\python\\app\\main\\Dal\\"
download_directory = "D:\\Tomer\\Learn\\python\\FreeTimeApp\\"

def is_good_mp3_file(full_file_name : str):
    """
    ************** Maybe change ****************
    :param full_file_name:
    :return:
    """
    try:
        temp_track = get_mp3_properties(full_file_name)
        if (temp_track.get("artist") is None) or (temp_track.get("title") is None):
            return False
        else:
            return True
    except Exception as e:
        print(e)



def fix_mp3_name(directory: str, title: str, artist: str):
    """
    ************** Maybe change ***************
    :param name:
    :param artist:
    :return:
    """
    fix_name = artist + ' - ' + title + mp3_end
    return directory + fix_name


def mp3_move_directory(src_directory: str,dest_directory: str, file_name: str):

    try:
        shutil.move(src_directory + file_name, dest_directory + file_name)
        print(file_name + " has moved from: " + src_directory + " to: " + dest_directory)
    except Exception as e:
        print(e)

def fix_downloading_mp3_name(directory: str, song_id: str, song_name: str, artist: str):
    """
    The function gives the mp3 file a meanfull name
    by the song name and the artist
    :param directory:
    :param song_id:
    :return: None
    """
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".mp3"):
                if name.find(song_id):
                    fixed_name = fix_mp3_name(directory, song_name, artist)
                    full_name = directory + name
                    os.rename(full_name, fixed_name)


def update_mp3_properties(full_name: str, title: str, artist: str):
    """
    The function updates the mp3 file's properties according the parameters
    :param full_name:
    :param wanted_name:
    :param artist:
    :param album:
    :param year:
    :return: None
    """
    audio = EasyID3(full_name)
    audio['title'] = title
    audio['artist'] = artist
    audio.save()


def get_mp3_properties(full_name: str):
    """
    The function gets file path and return the mp3 file's properties
    :param full_name:
    :return: object describe the mp3 file
    """
    audio = EasyID3(full_name)
    return audio

def download_song(artist: str, song_name: str):
    """
    The function gets wanted song name of wanted artist and download
    :param artist:
    :param song_name:
    :return:
    """
    query_string = urllib.parse.urlencode({"search_query": artist + " - " + song_name + " lyrics"})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + search_results[0]])
    fix_downloading_mp3_name(download_directory, search_results[0], song_name, artist)
    fixed_song_name = artist + " - " + song_name + mp3_end
    update_mp3_properties(download_directory + fixed_song_name, song_name, artist)
    data = mp3_to_json("", download_directory + fixed_song_name)
    mp3_move_directory(download_directory, "D:\\Tomer\\music-check\\", fixed_song_name)
    return data

def get_song_lyrics(artist: str, song_name: str):
    """
    The function get artist and the song and find the song's lyrics
    :param artist:
    :param song_name:
    :return: The wanted song's lyrics
    """
    lyrics = ""
    try:
        lyrics = lyricwikia.get_lyrics(artist, song_name)
        lyrics = str(lyrics).replace("'", "''")
    except Exception as e:
        lyrics = "No Lyrics has found to this song"
    finally:
        return lyrics

def get_mp3_length(full_name: str):
    """

    :param full_name:
    :return:
    """
    mp3_file = MP3(full_name)
    total = int(mp3_file.info.length)
    minutes = int(total / 60)
    seconds = total - (minutes * 60)
    length = str(minutes) + ":"
    if seconds < 10:
        length  = length + "0" + str(seconds)
    else:
        length = length + str(seconds)
    return  length


def mp3_to_json(self, full_name):
    """
    the function gets mp3 path and creates song json from it
    :param full_name:
    :return: A song in json format
    """
    json_object = {}
    try:
        song_details = get_mp3_properties(full_name)
        print(song_details)
        json_object["Title"] = song_details['title'][0] if not song_details['title'][0] is None else " "
        json_object["Artist"] = song_details['artist'][0] if not song_details['artist'][0] is None else " "
        json_object["Album"] = " "
        json_object["Year"] = " "
        json_object["Rate"] = "0.0"
        json_object["Length"] = get_mp3_length(full_name)
        json_object["Lyrics"] = get_song_lyrics(song_details['artist'][0], song_details['title'][0])
    except Exception as e:
        print(e)
    finally:
        return json_object


def create_json_file_from_mp3(source_directory:str, dest_directory:str, song_name:str):
    """

    :param source_directory:
    :param dest_directory:
    :param song_name:
    :return:
    """
    data = mp3_to_json("",source_directory + song_name)
    current_file = open(dest_directory + "\\" + song_name.split(".mp3")[0] + ".json", "w+")
    current_file.write(str(data))
    current_file.close()

def download_songs_from_file(songs_for_download_file: str):
    """
    The function get sucess scan result file name and creates for each file json file
    :param scan_fesult_file_name:
    :param files_directory:
    :return: None
    """
    print("Downloads began at: " + datetime.datetime.now().strftime("%H:%M:%S"))

    with open(songs_for_download_file) as download_songs_file:
        content = download_songs_file.readlines()
        content = [x.strip() for x in content]
        for wanted_song in content:
            try:
                artist, song_name = wanted_song.split(' - ')
                download_song(artist, song_name)
            except Exception as e:
                print(e)

    print("Downloads ended at: " + datetime.datetime.now().strftime("%H:%M:%S"))

def find_json(name:str):
    """
    The function gives the mp3 file a meanfull name
    by the song name and the artist
    :param directory:
    :param song_id:
    :return: None
    """
    data = {}
    try:
        current_file = open('D:\\Tomer\\Music metadata' + "\\" + name +".json", "r+")
        data = json.load(current_file)
    except Exception as e:
        print(e)
    return data




if __name__ == '__main__':
    download_songs_from_file("D:\\Tomer\\Learn\\python\\app\\main\\Dal\\songs_for_download.txt")
