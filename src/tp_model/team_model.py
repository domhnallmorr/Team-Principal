import copy
import logging
import random
from tp_model import car_model

class Team:
	def __init__(self, model, name, car_speed, car_failure_probability, nationality, headquarters, tp,
			  technical_director, drivers_championships, constructors_championships, wins,
			  wind_tunnel, super_computer, engine_factory, chassis_workshop, brake_center,
			  workforce):
		self.model = model
		self.car = car_model.Car(self, car_speed, car_failure_probability)
		self.name = name
		self.nationality = nationality
		self.headquarters = headquarters
		self.team_principal = tp
		self.technical_director = technical_director
		
		# FACILITIES
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
		self.wind_tunnel_tracker = [self.wind_tunnel]

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
			driver = self.model.get_instance_by_name(driver, "Driver")
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

		facilities = ["windtunnel", "super computer", "engine factory", "chassis workshop", "brake center"]
		facility_variables = [self.wind_tunnel, self.super_computer, self.engine_factory, self.chassis_workshop, self.brake_center]

		# Determine if team upgrades facilities
		for idx, facility in enumerate(facility_variables):
			if facility < 60:
				should_upgrade = self.should_upgrade(facility)
				if should_upgrade is True:
					if idx == 0:
						self.wind_tunnel += random.randint(20, 40)
						if self.wind_tunnel > 100:
							self.wind_tunnel = 100

					elif idx == 1:
						self.super_computer += random.randint(20, 40)
						if self.super_computer > 100:
							self.super_computer = 100

					elif idx == 2:
						self.engine_factory += random.randint(20, 40)
						if self.engine_factory > 100:
							self.engine_factory = 100

					elif idx == 3:
						self.chassis_workshop += random.randint(20, 40)
						if self.chassis_workshop > 100:
							self.chassis_workshop = 100

					elif idx == 4:
						self.brake_center += random.randint(20, 40)
						if self.brake_center > 100:
							self.brake_center = 100

					self.model.inbox.generate_facility_update_email(self, facilities[idx])
	
		self.wind_tunnel_tracker.append(self.wind_tunnel)

	def should_upgrade(self, current_value):
		should_upgrade = False

		if current_value < 10:
			should_upgrade = True
		else:
			# Generate a random number between 0 and 1
			random_value = random.random()

			upgrade_threshold = 0.2  # Example: 30% chance of upgrading

			if random_value < upgrade_threshold:
				should_upgrade = True

		return should_upgrade