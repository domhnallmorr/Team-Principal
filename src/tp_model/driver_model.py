import logging
import random

import pandas as pd

from tp_model import email_model

class Driver:
	def __init__(self, model, image_data, nationality, name, age, hometown="",
	      championships=0, wins=0, races=0, podiums=0, speed=70, consistency=70):
		self.model = model
		self.image_data = image_data
		self.nationality = nationality
		self.hometown = hometown
		self.name = name
		self.age = age
		self.championships = championships
		self.wins = wins
		self.races = races
		self.podiums = podiums
		self.speed = speed
		self.consistency = consistency
		
		self.setup_variables()
		self.decide_when_retiring()

	def setup_variables(self):
		self.retired = False
		self.retiring = False
		self.week_to_annouce_retirement = 3

		self.team = None

		self.season_stats_df = pd.DataFrame(columns=["Year", "Races", "Wins", "Podiums", "Points", "DNFs"])

	def decide_when_retiring(self):
		self.retiring_age = random.randint(35, 42)
		if self.retiring_age < self.age:
			self.retiring_age = self.age + 1


	def increase_age(self):
		self.age += 1

		if self.retiring is True:
			self.retired = True
			self.retiring = False

		elif self.retired is False:
			if self.age == self.retiring_age:
				self.retiring = True
				print(f"{self.name} is retiring")
				self.model.inbox.generate_driver_retirement_email(self)
				

if __name__ == "__main__":
	import track_model
	track = track_model.Track()

	driver = Driver("Hamilton", 0.9, 0.97)

	for i in range(10):
		laptime = driver.calculate_laptime(track)
		print(round(laptime/1000, 3))