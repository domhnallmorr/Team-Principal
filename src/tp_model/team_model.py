import copy
import logging
import random
from datetime import datetime, timedelta

from tp_model import car_model

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
		self.update_historical_financial_data()

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
		self.balance = 5_762_308
		self.cost_per_race = 400_000
		self.average_staff_wage = 40_000
		self.staff_costs_per_week = int(self.average_staff_wage*self.workforce/52)
		self.sponsorship_income = 12_830_316

		self.balance_historical_data = []
		self.profit_loss_historical_data = []

		self.start_balance = self.balance
		self.profit_this_month = 0
		self.profit_this_season = 0
		self.profit_last_season = "-"
		# self.engine_costs = 7_000_000
		# self.tyre_costs = 3_000_000
		# self.chassis_costs = 5_000_000

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
			self.profit_last_season = self.profit_this_season
			self.profit_this_season = 0

			self.sponsorship_income = self.commercial_manager.negotiate_new_deal()
			self.model.inbox.new_sponsor_income_email(self)

	def end_season(self):
		self.update_facilities()

	def update_weekly_finances(self):
		self.balance -= self.staff_costs_per_week

		self.profit_this_season = self.balance - self.start_balance
		self.update_historical_financial_data()

	def account_for_race_costs(self):
		self.balance -= self.cost_per_race

		# sponsorship income
		self.balance += int(self.sponsorship_income/self.model.season.get_number_of_races())

	def update_historical_financial_data(self):
		self.balance_historical_data.append({"Timestamp": datetime(self.model.season.year, 1, 1) + timedelta(weeks=self.model.season.current_week - 1), "Balance": self.balance})

		# Remove data older than 2 years
		two_years_ago = self.model.season.year - 2
		self.balance_historical_data = [entry for entry in self.balance_historical_data if entry["Timestamp"].year >= two_years_ago]

		# Update profit/loss over last 4 weeks
		if len(self.balance_historical_data) >= 4:
			current_balance = self.balance_historical_data[-1]["Balance"]
			four_weeks_ago_balance = self.balance_historical_data[-4]["Balance"]
			self.profit_this_month = current_balance - four_weeks_ago_balance
			self.profit_loss_historical_data.append({"Timestamp": self.balance_historical_data[-1]["Timestamp"], "Profit_Loss": self.profit_this_month})
		else: # don't have 4 weeks of data yet
			self.profit_this_month = self.profit_this_season

		self.profit_loss_historical_data.append({"Timestamp": self.balance_historical_data[-1]["Timestamp"], "Profit_Loss": self.profit_this_month})

		# Remove data older than 2 years
		self.profit_loss_historical_data = [entry for entry in self.profit_loss_historical_data if entry["Timestamp"].year >= two_years_ago]

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

			
