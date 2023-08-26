import logging
import random

import pandas as pd

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

	def setup_variables(self):
		self.retired = False
		self.retiring = False
		self.week_to_annouce_retirement = 3

		self.team = None

		self.season_stats_df = pd.DataFrame(columns=["Year", "Races", "Wins", "Podiums"])

	def calculate_laptime(self, track):
		# Simulate laptime calculation based on driver's speed and track's grip
		laptime = track.base_laptime / (self.speed * track.grip)

		# Add inconsistency factor with random variation
		inconsistency_factor = 0.1 * (1 - self.consistency)
		random_variation = random.uniform(0.0, inconsistency_factor)
		laptime += laptime * random_variation

		self.race_time += laptime

		return laptime

	def update_position(self, position):
		self.position = position	

	def decide_if_retiring(self):
		if self.name not in self.model.season.drivers_hired_for_next_season: # avoid a driver who's just been hired for season deciding to retire
			if self.age > 40:
				self.retiring = True
			elif self.age > 35:
				if random.random() > 0.5:
					self.retiring = True
					
		if self.retiring is True:
			logging.info(f"DRIVER RETIREMENT: {self.name}")
			if self.team is not None:
				self.team.hire_new_driver(self.name)
				
		if self.retiring is False:
			if self.team is not None:
				self.team.retain_driver(self.name)

	def increase_age(self):
		self.age += 1


if __name__ == "__main__":
	import track_model
	track = track_model.Track()

	driver = Driver("Hamilton", 0.9, 0.97)

	for i in range(10):
		laptime = driver.calculate_laptime(track)
		print(round(laptime/1000, 3))