import datetime
import os
from tinytag import TinyTag, TinyTagException 

print(datetime.datetime.now())

directory = "D:\\Tomer\\music-check"
print(datetime.datetime.now())

tracks = []

for root, die, files in os.walk(directory):
	for name in files:
		if name.endswith(".mp3"):
			try:		
				tracks.append(name)
				temp_track = TinyTag.get(root + "\\" + name)
				print(temp_track.artist + " - " + temp_track.title)
			except Exception as e:
				print("There was a problem with the song- " + name)
print(datetime.datetime.now())