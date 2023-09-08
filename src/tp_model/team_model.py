import copy
import logging
import random
from tp_model import car_model

class Team:
	def __init__(self, model, name, car_speed, car_failure_probability, nationality, headquarters, tp,
			  drivers_championships, constructors_championships, wins,
			  wind_tunnel, super_computer, engine_factory, chassis_workshop, brake_center,
			  workforce):
		self.model = model
		self.car = car_model.Car(self, car_speed, car_failure_probability)
		self.name = name
		self.nationality = nationality
		self.headquarters = headquarters
		self.team_principal = tp
		self.wind_tunnel = wind_tunnel
		self.super_computer = super_computer
		self.engine_factory = engine_factory
		self.chassis_workshop = chassis_workshop
		self.brake_center = brake_center
		self.workforce = workforce

		# STATS
		self.drivers_championships = drivers_championships
		self.constructors_championships = constructors_championships
		self.wins = wins
		
		self.setup_variables()

	def setup_variables(self):
		self.is_player_team = False
		self.drivers = [None, None]
		self.drivers_next_year = [None, None]

		self.driver_changes_next_year = []

		# Facilities
		self.wind_tunnel_last_upgrade_year = None # when the tunnel was last upgraded

		# FINANCIAL STUFF
		self.budget = 25_000_000
		self.balance = 1_000_000
		self.cost_per_race = 400_000
		self.average_staff_wage = 40_000
		self.number_of_staff = 80
		self.staff_costs = self.average_staff_wage*self.number_of_staff
		self.engine_costs = 7_000_000
		self.tyre_costs = 3_000_000
		self.chassis_costs = 5_000_000

		# SPONSERS
		self.engine_cover_sponser = None
		self.rear_wing_sponser = None
		self.front_wing_sponser = None
		self.sidepod_sponser = None

		self.engine_cover_sponser_next_year = None
		self.rear_wing_sponser_next_year = None
		self.front_wing_sponser_next_year = None
		self.sidepod_sponser_next_year = None

		# PRIZE MONEY
		self.prize_money = 0

	def set_drivers_team(self):
		for driver in self.drivers:
			driver = self.model.get_driver_from_name(driver)
			driver.team = self

	def hire_new_driver(self, current_driver, free_agents):
		replacement = random.choice(free_agents)
		idx = self.drivers_next_year.index(current_driver.name)
		self.drivers_next_year[idx] = replacement.name
		self.model.inbox.generate_driver_hiring_email(self, replacement)

		return replacement

	def update_drivers_for_new_season(self):
		self.drivers = copy.deepcopy(self.drivers_next_year)

	def end_season(self):
		self.update_facilities()

	def update_facilities(self):
		self.wind_tunnel -= 4
		if self.wind_tunnel < 1:
			self.wind_tunnel = 1

		# Determine if team upgrades facilities
		# for facility in [self.wind_tunnel]:
		# 	if facility < 60:
	
	def should_upgrade(self, current_value, last_upgrade_year):
		should_upgrade = False

		# Generate a random number between 0 and 1
		random_value = random.random()
        # Set a threshold for the upgrade decision (adjust as needed)
		upgrade_threshold = 0.3  # Example: 30% chance of upgrading
        # Compare the random number to the threshold
    	# return random_value < upgrade_threshold

		return should_upgrade