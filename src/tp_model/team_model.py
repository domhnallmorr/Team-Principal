import copy
import logging
import random


from tp_model import car_model, team_finance_model

class Team:
	def __init__(self, model, name, car_speed, car_failure_probability, nationality, headquarters, tp,
			  technical_director, drivers_championships, constructors_championships, wins,
			  wind_tunnel, super_computer, engine_factory, chassis_workshop, brake_center,
			  workforce, commercial_manager):
		self.model = model
		self.car = car_model.Car(self, car_speed, car_failure_probability)
		self.name = name
		self.nationality = nationality
		self.headquarters = headquarters
		
		# STAFF
		self.team_principal = tp
		self.technical_director = technical_director
		self.technical_director.team = self
		
		self.commercial_manager = commercial_manager
		self.commercial_manager.team = self
		
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

		self.position_last_year = None

		# Facilities
		self.wind_tunnel_last_upgrade_year = None # when the tunnel was last upgraded
		self.wind_tunnel_tracker = [self.wind_tunnel]

		# FINANCIAL STUFF
		balance = 5_762_308
		self.finance_model = team_finance_model.TeamFinance(self, balance)

		# STAFF
		self.commercial_manager_next_year = None

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

	def new_season(self):

		if self.model.player_team == self:
			# FINANCIAL STUFF
			self.finance_model.new_season()

			if self.commercial_manager_next_year is not None:
				self.commercial_manager = self.commercial_manager_next_year

	def end_season(self):
		if self.model.player_team != self:
			self.update_facilities()

		for idx, team in enumerate(self.model.season.team_standings):
			if team[0] == self.name:
				self.position_last_year = idx + 1

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
	
	def hire_technical_director(self, force_hire=False):

		random_value = random.random()

		if random_value < 0.2 or force_hire is True: # 20% chance they want to hire new TD
			available_tds = [td for td in self.model.technical_directors if td.wants_to_move is True or td.team is None]

			current_td = self.technical_director
			if current_td in available_tds:
				available_tds.remove(current_td)

			if available_tds != []:
				new_td = random.choice(available_tds)

				if new_td.team is not None: # if currently employed
					new_td.team.technical_director = None # set his current team TD to None
				
				if current_td is not None:
					current_td.team = None

				self.technical_director = new_td
				self.technical_director.team = self
				self.technical_director.wants_to_move = False

				self.model.inbox.new_technical_director_email(self, self.technical_director)

			

	
	def upgrade_player_facility(self, data):
		
		if data["upgrade_type"].lower() == "minor":
			upgrade = random.randint(10, 25)
			cost = 3_000_000
		else:
			upgrade = random.randint(40, 60)
			cost = 15_000_000

		if data["facility"].lower() == "wind tunnel":
			self.wind_tunnel += upgrade
			if self.wind_tunnel > 100:
				self.wind_tunnel = 100

		elif data["facility"].lower() == "super computer":
			self.super_computer += upgrade
			if self.super_computer > 100:
				self.super_computer = 100

		elif data["facility"].lower() == "engine factory":
			self.engine_factory += upgrade
			if self.engine_factory > 100:
				self.engine_factory = 100

		elif data["facility"].lower() == "chassis workshop":
			self.chassis_workshop += upgrade
			if self.chassis_workshop > 100:
				self.chassis_workshop = 100

		elif data["facility"].lower() == "brake center":
			self.brake_center += upgrade
			if self.brake_center > 100:
				self.brake_center = 100

		else:
			raise Exception(f"Unknown facility {data['facility']}")

		self.finance_model.update_balance("cost", cost, "facility_upgrade")

		