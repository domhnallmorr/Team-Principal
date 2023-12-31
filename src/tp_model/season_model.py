import copy
import logging
import random

from tp_model import checking_functions, driver_database, team_database

class Season:
	def __init__(self, model):
		self.model = model
		self.setup_variables()
	
	def setup_variables(self):
		self.year = 1998
		self.current_week = 1
		self.calender = [
			[8, "Race of Australia", "Alexandra Park", "Melbourne", "Australia"], # Wk Number, title, circuit, city, country 
			[10, "Race of Brasil", "Perus", "Sao Paulo", "Brazil"],
			[12, "Race of Argentina", "Villa Riachuelo", "Buenos Aires", "Argentina"],
			[14, "Race of San Marino", "Simona", "Imola", "Italy"],
			[16, "Race of Spain", "Circuit de Barcelona", "Barcelona", "Spain"],
			[18, "Race of Monaco", "Monaco Street Track", "Monte Carlo", "Monaco"],
			[20, "Race of Canada", "Montreal Street Track", "Montreal", "Canada"],
			[22, "Race of France", "Circuit de France", "Magny Cours", "France"],
			[24, "Race of UK", "Bronze Rock", "Northampton", "UK"],
			[26, "Race of Austria", "B2 Ring", "Speilberg", "Austria"],
			[28, "Race of Germany", "Walldorfring", "walldorf", "Germany"],
			[30, "Race of Hungary", "Budapestring", "Budapest", "Hungary"],
			[32, "Race of Belgium", "Ardennesring", "Stavelot", "Belgium"],
			[34, "Race of Italy", "Lambro", "Monza", "Italy"],
			[36, "Race of Luxembourg", "Eifelring", "Nurburg", "Germany"],
			[38, "Race of Japan", "Mie Circuit", "Suzuka", "Japan"],
		]

		self.current_round = 0
		self.drivers = []

		self.points_system = [10, 6, 4, 3, 2, 1]
		self.driver_standings = []
		self.team_standings = []
		self.drivers_hired_for_next_season = []
		self.previous_results = {}

	def get_next_race_text(self):
		if self.current_round >= len(self.calender):
			return "Off-Season"
		else:
			return f"{self.calender[self.current_round][1]} Week {self.calender[self.current_round][0]}"

	def get_number_of_races(self):
		return len(self.calender)

	def setup_initial_standings(self):
		self.driver_standings = []
		self.team_standings = [[t.name, 0] for t in self.model.teams]

		for t in self.model.teams:
			self.driver_standings.append([t.drivers[0], 0])
			self.driver_standings.append([t.drivers[1], 0])

	def update_standings(self, result):

		for idx, points in enumerate(self.points_system):
			driver_name = result[idx][0]
			for d in self.driver_standings:
				if d[0] == driver_name:
					d[1] += points

					# ADD POINTS TO TEAM
					for team in self.team_standings:
						if driver_name in self.model.get_instance_by_name(team[0], "Team").drivers:
							team[1] += points
							break

					break
		
		self.driver_standings = sorted(self.driver_standings, key=lambda x: x[1], reverse=True)
		self.team_standings = sorted(self.team_standings, key=lambda x: x[1], reverse=True)

	def end_race_weekend(self):
		self.current_week += 1
		self.current_round += 1

	def end_season(self):
		self.current_round = "off_season"

		# UPDATE STATS
		self.champion = self.driver_standings[0][0]
		driver = self.model.get_instance_by_name(self.champion, "Driver")
		driver.championships += 1
		driver.team.drivers_championships += 1

		self.constructors_champion = self.team_standings[0][0]
		team = self.model.get_instance_by_name(self.constructors_champion, "Team")
		team.constructors_championships += 1

		# UPDATE CARS
		for team in self.model.teams:
			team.car.update_car_speed() # Random change in car speed
			team.update_drivers_for_new_season()

		# Update all drivers teams
		for driver in self.model.drivers:
			driver.team = None
			for team in self.model.teams:
				if driver.name in team.drivers:
					driver.team = team

		# Update Teams
		for team in self.model.teams:
			team.end_season()

	def setup_new_season(self, update_year=True):
		self.current_week = 1
		self.current_round = 0
		
		if update_year is True:
			self.year += 1

		# Add new row to driver statistics
		for driver in self.model.drivers:
			driver.season_stats_df.loc[self.year] = 0
			driver.season_stats_df.at[self.year, "Year"] = self.year
			
			if update_year is True:
				driver.increase_age()

		# Add drivers/staff
		team_database.add_commercial_mangers(self.model, self.year)
		driver_database.add_drivers(self.model, self.year)

		self.setup_initial_standings()
		self.handle_driver_retirements()

		# Track results
		self.previous_results[self.year] = copy.deepcopy(self.calender)

		# Update teams
		if update_year is True:
			for team in self.model.teams:
				team.new_season()

		# Handle Technical_directors switching teams
		team_database.add_technical_directors(self.model, self.year)

		if update_year is True:
			for td in self.model.technical_directors:
				td.decide_switch_teams()

			for team in self.model.teams:
				team.hire_technical_director()

			# Ensure all teams have a TD
			for idx in [0, 1, 2]: # this is very crude, need to figure why it's neeeded
				for team in self.model.teams:
					if team.technical_director is None:
						team.hire_technical_director(force_hire=True)

			checking_functions.technical_director_switch_teams_checks(self.model)

	def handle_driver_retirements(self):
		free_agents = [d for d in self.model.drivers if d.team is None and d.retired is False and d.retiring is False]
		retiring_drivers = [d for d in self.model.drivers if d.retiring is True]

		for retiring_driver in retiring_drivers:
			if retiring_driver.team is not None: # currently employed driver
				replacement = retiring_driver.team.hire_new_driver(retiring_driver, free_agents)
				free_agents.remove(replacement)

	def get_next_track(self):
		return self.calender[self.current_round][2]