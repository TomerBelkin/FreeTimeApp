import json
import sys
import spotipy
import spotipy.util as util

def get_artist(artist):
    scope = 'user-library-read'
    username = "x2do2llexubo56grhqqcfhmte"

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.search(artist,1,0,"artist")
        current_artist_id = results["artists"]["items"][0]["id"]
        print(current_artist_id)
    else:
        print("Can't get token for " + username)


if __name__ == '__main__':
    get_artist("coldplay")
