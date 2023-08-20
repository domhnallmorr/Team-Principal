import os
import sqlite3
from tp_model import driver_model

def add_drivers(model, year):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM drivers WHERE Year_Appear = '{str(year)}'")
	drivers = cursor.fetchall()

	for driver in drivers:
		image_data = driver[4]
		nationality = driver[5]
		championships = driver[6]
		wins = driver[7]

		model.drivers.append(driver_model.Driver(model, image_data, nationality, 
					   driver[0], driver[2], championships, wins,
					   driver[1],
					   								))
