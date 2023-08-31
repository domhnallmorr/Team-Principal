import os
import sqlite3
import random

from tp_model import driver_database, season_model, team_model, track_database
from race_model import race_model, participant

class TPModel:
	def __init__(self):
		self.setup_variables()
		self.season = season_model.Season(self)

		self.setup_default_drivers()
		self.setup_default_teams()
		self.setup_tracks()
		self.season.setup_new_season(update_year=False)

	def setup_variables(self):
		self.drivers = []
		self.teams = []
		self.tracks = []
		
		self.in_race_week = False
		self.race_result = None

	def setup_default_drivers(self):
		driver_database.add_drivers(self, "default")

	def setup_default_teams(self):
		conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM teams")
		teams = cursor.fetchall()

		for team in teams:
			self.teams.append(team_model.Team(self, team[0], team[1], team[2]))
			self.teams[-1].drivers = [team[3], team[4]]
			self.teams[-1].drivers_next_year = [team[3], team[4]]
		self.season.setup_initial_standings()

		for team in self.teams:
			team.set_drivers_team()
			team.drivers_next_year = team.drivers

		# SETUP PRIZE MONEY
		self.teams[-1].prize_money = 7_000_000

	def setup_tracks(self):
		track_database.add_tracks(self)

	def get_main_window_data(self):
		data = {}

		if self.season.current_round != "off_season":
			data["date"] = f"Week {self.season.current_week} - Next Race: {self.season.year}\t{self.season.get_next_race_text()}"
		else:
			data["date"] = f"Week {self.season.current_week} - Off Season"
		data["in_race_week"] = self.in_race_week

		return data

	def get_calender_window_data(self):
		data = {}

		data["calender"] = self.season.calender
  
		return data
		
	def get_standings_window_data(self):
		data = {}
		data["driver_standings"] = self.season.driver_standings
		data["team_standings"] = self.season.team_standings
  
		return data

	def get_results_window_data(self):
		data = {}
		data["results"] = self.race_result
  
		return data
	
	def get_race_weekend_data(self):
		data = {}
		track = self.get_track_from_name(self.season.get_next_track())

		data["name"] = track.name
		data["laps"] = track.no_of_laps
		data["length"] = round(track.length/1000, 3)

		return data

	def get_driver_window_data(self, driver):
		data = {}

		data["name"] = driver
		driver = self.get_driver_from_name(driver)
		data["age"] = driver.age
		data["nationality"] = driver.nationality
		data["hometown"] = driver.hometown
		data["team"] = driver.team.name
		data["championships"] = driver.championships
		data["wins"] = driver.wins
		data["races"] = driver.races
		data["podiums"] = driver.podiums
		data["seasons_data"] = driver.season_stats_df.values.tolist()

		return data

	def get_circuit_window_data(self, track):
		data = {}

		data["name"] = track
		track = self.get_track_from_name(track)
		data["description"] = track.description
		data["city"] = track.city
		data["country"] = track.country
		data["length"] = round(track.length/1000, 3)
		data["laps"] = track.no_of_laps

		data["downforce"] = track.downforce
		data["grip"] = track.grip
		data["top_speed"] = track.top_speed
		data["braking"] = track.braking
		
		return data

	def advance(self):
		# self.in_race_week = False

		if self.in_race_week is False:
			self.advance_one_week()

	
	
	def advance_one_week(self):
		self.season.current_week += 1

		if self.season.current_week == 53:
			self.season.setup_new_season()
		else:
			if self.season.current_round != "off_season":
				if self.season.current_week == self.season.calender[self.season.current_round][0]:
					self.in_race_week = True
				else:
					self.in_race_week = False

	def get_driver_from_name(self, name):
		driver = None

		for d in self.drivers:
			if d.name == name:
				driver = d
				return driver
		if driver is None:
			print(f"Can't find {driver}")

	def get_team_from_name(self, name):
		team = None

		for team in self.teams:
			if team.name == name:
				break
		return team

	def get_track_from_name(self, name):
		track = None

		for track in self.tracks:
			if track.name == name:
				return track

	def simulate_race(self):
		track = self.get_track_from_name(self.season.get_next_track())
		participants = []
		for d in self.drivers:
			if d.team is not None:
				car = d.team.car
				participants.append(participant.Participant(d, car, track))

		self.race_model = race_model.RaceModel(participants, track)
		
		self.race_result = self.race_model.race_result
		self.season.update_standings(self.race_result)
		self.update_driver_stats(self.race_result)

		self.in_race_week = False
		self.season.current_round += 1

		if self.season.current_round == len(self.season.calender):
			self.season.end_season()

	def get_driver_image_data(self):
		return {d.name: d.image_data for d in self.drivers}
	
	def update_driver_stats(self, race_result):
		for idx, d in enumerate(race_result):
			driver = self.get_driver_from_name(d[0])
			driver.races += 1
			driver.season_stats_df.loc[self.season.year, "Races"] += 1

			if idx == 0: # wins
				driver.wins += 1
				driver.podiums += 1
				driver.season_stats_df.loc[self.season.year, "Wins"] += 1
				driver.season_stats_df.loc[self.season.year, "Podiums"] += 1
			
			if idx == 1 or idx == 2: # Podiums
				driver.podiums += 1
				driver.season_stats_df.loc[self.season.year, "Podiums"] += 1