import os
import sqlite3
import random

from tp_model import driver_database, email_model, season_model, team_model, track_database, team_database
from race_model import race_model, participant

class TPModel:
	def __init__(self, mode="ui-player"):
		self.mode = mode
		self.setup_variables()
		self.season = season_model.Season(self)

		self.setup_default_drivers()
		team_database.add_team_principals(self, "default")
		team_database.add_technical_directors(self, "default")
		team_database.add_commercial_mangers(self, "default")
		team_database.add_teams(self)

		self.setup_tracks()
		self.season.setup_new_season(update_year=False)

		self.player_team = self.get_instance_by_name("Moretti", "Team")
		self.player_team.is_player_team = True

	def setup_variables(self):
		self.drivers = []
		self.teams = []
		self.tracks = []
		self.team_principals = []
		self.technical_directors = []
		self.commercial_managers = []
		
		self.in_race_week = False
		self.race_result = None

		self.inbox = email_model.Inbox(self)

	def setup_default_drivers(self):
		driver_database.add_drivers(self, "default")

	def setup_tracks(self):
		track_database.add_tracks(self)
	
	def get_race_weekend_data(self):
		data = {}
		track = self.get_instance_by_name(self.season.get_next_track(), "Track")

		data["name"] = track.name
		data["laps"] = track.no_of_laps
		data["length"] = round(track.length/1000, 3)

		return data

	def advance(self):
		is_new_seaason = False

		if self.in_race_week is False:
			is_new_seaason = self.advance_one_week()
		elif self.mode == "headless":
			self.simulate_race()

		return is_new_seaason	
	
	def advance_one_week(self):
		self.inbox.new_mails = 0
		new_season = False

		self.season.current_week += 1

		if self.mode == "ui-player":
			self.player_team.update_weekly_finances()

		if self.season.current_week == 53:
			self.season.setup_new_season()
			new_season = True
		else:
			if self.season.current_round != "off_season":
				if self.season.current_week == self.season.calender[self.season.current_round][0]:
					self.in_race_week = True
					if self.mode == "ui-player":
						self.player_team.account_for_race_costs()	

				else:
					self.in_race_week = False

		return new_season
	
	def get_instance_by_name(self, name, class_type):
		instance_list = None
        
		if class_type == "Team":
			instance_list = self.teams
		elif class_type == "commercialManager":
			instance_list = self.commercial_managers
		elif class_type == "Driver":
			instance_list = self.drivers
		elif class_type == "TeamPrincipal":
			instance_list = self.team_principals
		elif class_type == "TechnicalDirector":
			instance_list = self.technical_directors
		elif class_type == "Track":
			instance_list = self.tracks
			
		if instance_list is not None:
			for instance in instance_list:
				if instance.name == name:
					return instance
        
		return None


	def simulate_race(self):
		track = self.get_instance_by_name(self.season.get_next_track(), "Track")
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

		# Track results
		self.season.previous_results[self.season.year][self.season.current_round].append(self.race_result)
		self.season.current_round += 1

		if self.season.current_round == len(self.season.calender):
			self.season.end_season()

	def setup_race(self, run_race=True):
		track = self.get_instance_by_name(self.season.get_next_track(), "Track")
		participants = []
		for d in self.drivers:
			if d.team is not None:
				car = d.team.car
				participants.append(participant.Participant(d, car, track))

		self.race_model = race_model.RaceModel(participants, track, run_race)

	def get_driver_image_data(self):
		return {d.name: d.image_data for d in self.drivers}
	
	def update_driver_stats(self, race_result):
		for idx, d in enumerate(race_result):
			driver = self.get_instance_by_name(d[0], "Driver")
			driver.races += 1
			driver.season_stats_df.loc[self.season.year, "Races"] += 1
			
			if idx == 0: # wins
				driver.wins += 1
				driver.podiums += 1
				driver.season_stats_df.loc[self.season.year, "Wins"] += 1
				driver.season_stats_df.loc[self.season.year, "Podiums"] += 1

				driver.team.wins += 1
			
			if idx == 1 or idx == 2: # Podiums
				driver.podiums += 1
				driver.season_stats_df.loc[self.season.year, "Podiums"] += 1

			if idx < len(self.season.points_system): # Points
				driver.season_stats_df.loc[self.season.year, "Points"] += self.season.points_system[idx]

			if "dnf" in d[2].lower(): # DNFs
				driver.season_stats_df.loc[self.season.year, "DNFs"] += 1

		for idx, d in enumerate(self.season.driver_standings):
			driver = self.get_instance_by_name(d[0], "Driver")
			driver.season_stats_df.loc[self.season.year, "Pos"] = idx + 1


