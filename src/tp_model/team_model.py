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

	def hire_new_driver(self, driver_to_replace):
		available_drivers = self.model.find_free_agents()
		names = [d.name for d in available_drivers]

		new_driver = available_drivers[random.randint(0, len(available_drivers)-1)]

		idx = self.drivers.index(driver_to_replace)
		self.drivers_next_year[idx] = new_driver.name 

		self.driver_changes_next_year.append(f"{driver_to_replace} will be replaced by {new_driver.name}")
		self.model.season.drivers_hired_for_next_season.append(new_driver.name)
		

	def retain_driver(self, driver_to_retain):
		idx = self.drivers.index(driver_to_retain)
		self.drivers_next_year[idx] = driver_to_retain

	def setup_drivers_for_new_season(self):
		self.drivers = self.drivers_next_year
		self.drivers_next_year = self.drivers # Assume drivers will be retained.
		self.driver_changes_next_year = []
		
		for driver in self.drivers:
			self.model.get_driver_from_name(driver).team = self

	def account_for_race_cost(self):
		start_balance = self.balance
		self.balance -= self.cost_per_race

		for sponsor in list(set([self.engine_cover_sponser, self.rear_wing_sponser, self.front_wing_sponser, self.sidepod_sponser])):
			sponsor.make_payment()
		# RECIEVE PRIZE MONEY
		self.balance += int(self.prize_money/self.model.season.get_number_of_races())
		

	def account_for_weekly_costs(self):
		# STAFF
		self.balance -= self.staff_costs/self.model.number_of_weeks_in_season
		self.balance -= self.engine_costs/self.model.number_of_weeks_in_season
		self.balance -= self.tyre_costs/self.model.number_of_weeks_in_season
		self.balance -= self.chassis_costs/self.model.number_of_weeks_in_season
		
		self.balance = int(self.balance)
		
	def get_finance_data_for_view(self):
		data = {}
		data["staff_costs"] = self.staff_costs
		data["engine_costs"] = self.engine_costs
		data["chassis_costs"] = self.chassis_costs
		data["tyre_costs"] = self.tyre_costs
		data["race_costs"] = int(self.cost_per_race*len(self.model.season.calender))

		data["total_general_costs"] = self.staff_costs + self.chassis_costs + data["race_costs"] + self.tyre_costs + self.engine_costs

		data["engine_cover_sponsor"] = self.engine_cover_sponser.name
		data["engine_cover_payment"] = self.engine_cover_sponser.engine_cover_payment
		data["rear_wing_sponsor"] = self.rear_wing_sponser.name
		data["rear_wing_payment"] = self.rear_wing_sponser.rear_wing_payment
		data["front_wing_sponsor"] = self.front_wing_sponser.name
		data["front_wing_payment"] = self.front_wing_sponser.front_wing_payment
		data["sidepod_sponsor"] = self.sidepod_sponser.name
		data["sidepod_payment"] = self.sidepod_sponser.sidepod_payment

		data["total_sponsorship"] = self.engine_cover_sponser.engine_cover_payment + self.rear_wing_sponser.rear_wing_payment + self.front_wing_sponser.front_wing_payment + self.sidepod_sponser.sidepod_payment
		
		data["prize_money"] = self.prize_money

		data["total_income"] = self.prize_money + data["total_sponsorship"]

		return data
	
	def get_sponsor_data_for_view(self):
		data = []
		if self.engine_cover_sponser is not None:
			data.append([self.engine_cover_sponser.name, "Engine Cover", f"${self.engine_cover_sponser.engine_cover_payment:,}", str(self.engine_cover_sponser.years_left_on_contract)])
		if self.front_wing_sponser is not None:
			data.append([self.front_wing_sponser.name, "Front Wing", f"${self.front_wing_sponser.front_wing_payment:,}", str(self.front_wing_sponser.years_left_on_contract)])
		if self.rear_wing_sponser is not None:
			data.append([self.rear_wing_sponser.name, "Rear Wing", f"${self.rear_wing_sponser.rear_wing_payment:,}", str(self.rear_wing_sponser.years_left_on_contract)])
		if self.sidepod_sponser is not None:
			data.append([self.sidepod_sponser.name, "Sidepod", f"${self.sidepod_sponser.sidepod_payment:,}", str(self.sidepod_sponser.years_left_on_contract)])

		return data
	
	def sponser_deal_agreed(self, data):
		if data["location"] == "Engine Cover":
			self.engine_cover_sponser_next_year = data["sponsor"]