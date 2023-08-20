import os
import sqlite3
from tp_model import track_model

def add_tracks(model):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM tracks")
	tracks = cursor.fetchall()

	for track in tracks:
		name = track[0]
		city = track[1]
		country = track[2]
		title = track[3]
		length = track[4] # in meters 
		laps = track[5]
		track_map = track[6] # base 64
		description = track[7] # base 64

		downforce = track[8]
		grip = track[9]
		top_speed = track[10]
		braking = track[11]

		model.tracks.append(track_model.TrackModel(name, city, country, length, laps, track_map, description,
					    downforce, grip, top_speed, braking))
	