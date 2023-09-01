import os
import sqlite3
from tp_model import driver_model

def add_drivers(model, year):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")

	# GET COLUMN NAMES
	table_name = "drivers"
	cursor = conn.execute(f'PRAGMA table_info({table_name})')
	columns = cursor.fetchall()
	column_names = [column[1] for column in columns]

	# GET COLUMN INDECES
	name_idx = column_names.index("Name")
	age_idx = column_names.index("Age")
	speed_idx = column_names.index("Speed")
	image_idx = column_names.index("Image")
	nation_idx = column_names.index("Nationality")
	titles_idx = column_names.index("Championships")
	wins_idx = column_names.index("Number of Wins")
	races_idx = column_names.index("Number of Races")
	hometown_idx = column_names.index("Hometown")
	podiums_idx = column_names.index("Podiums")

	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM drivers WHERE Year_Appear = '{str(year)}'")
	drivers = cursor.fetchall()

	for driver in drivers:
		name = driver[name_idx]
		age = driver[age_idx]
		speed = driver[speed_idx]
		image_data = driver[image_idx]
		nationality = driver[nation_idx]
		hometown = driver[hometown_idx]
		championships = driver[titles_idx]
		wins = driver[wins_idx]
		races = driver[races_idx]
		podiums = driver[podiums_idx]

		model.drivers.append(driver_model.Driver(model, image_data, nationality,
					   name, age, hometown, championships, wins, races, podiums,
					   speed,))
