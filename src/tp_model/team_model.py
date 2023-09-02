import copy
import logging
import random
from tp_model import car_model

class Team:
	def __init__(self, model, name, car_speed, car_failure_probability):
		self.model = model
		self.car = car_model.Car(self, car_speed, car_failure_probability)
		self.name = name
		self.setup_variables()

	def setup_variables(self):
		self.is_player_team = False
		self.drivers = [None, None]
		self.drivers_next_year = [None, None]

		self.driver_changes_next_year = []

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

	def update_drivers_for_new_season(self):
		self.drivers = copy.deepcopy(self.drivers_next_year)
