from datetime import datetime, timedelta
import random

class TeamFinance:
	def __init__(self, team, initial_balance):
		self.team = team
		self.model = self.team.model

		self.balance = initial_balance

		self.cost_per_race = 400_000
		self.average_staff_wage = 40_000
		self.sponsorship_income = 12_830_316
		self.merchandise_income = 0
		self.prize_money = 5_000_000

		self.balance_historical_data = []
		self.profit_loss_historical_data = []

		self.start_balance = self.balance
		self.profit_this_month = 0
		self.profit_this_season = 0
		self.profit_last_season = "-"

		self.update_weekly_costs_income()
		self.update_historical_financial_data()

	def update_weekly_costs_income(self):
		self.staff_costs_per_week = int(self.average_staff_wage*self.team.workforce/52)
		self.sponsor_income_per_week = int(self.sponsorship_income/52)
		self.prize_money_per_week = int(self.prize_money/52)

	def update_weekly_finances(self):
		# STAFF
		self.update_balance("cost", self.staff_costs_per_week, "staff_cost")

		# PRIZE MONEY
		self.update_balance("income", self.prize_money_per_week, "prize_money")		
		
		# MERCH
		self.merchandise_income = self.calculate_merchandise_income()
		self.update_balance("income", self.merchandise_income, "merchandise sales")

	def account_for_race_costs(self):
		self.update_balance("cost", self.cost_per_race, "race_cost")

		# sponsorship income
		income = int(self.sponsorship_income/self.model.season.get_number_of_races())
		self.update_balance("income", income, "sponsorship")

	def update_balance(self, update_type, value, msg):
		
		assert update_type in ["cost", "income"], f"Unrecognised update_type {update_type}"
		
		if update_type == "cost":
			self.balance -= value
		elif update_type == "income":
			self.balance += value

		self.profit_this_season = self.balance - self.start_balance
		self.update_historical_financial_data()

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

	def calculate_merchandise_income(self):
		if self.model.season.current_round == "off_season":
			income = random.randint(5_000, 8_000)
		else:
			income = random.randint(15_000, 30_000)
		
		return income

	def new_season(self):	
		# FINANCIAL STUFF
		self.profit_last_season = self.profit_this_season
		self.profit_this_season = 0

		self.sponsorship_income = self.team.commercial_manager.negotiate_new_deal()
		self.model.inbox.new_sponsor_income_email(self.team)

		# PRIZE MONEY
		prize_money = [85_000_000, 70_000_000, 59_000_000, 47_000_000, 37_000_000, 31_000_000, 27_000_000, 22_000_000, 17_000_000, 12_000_000, 9_000_000]

		self.prize_money = prize_money[self.team.position_last_year-1] + random.randint(-3_000_000, 5_000_000)
		self.model.inbox.new_prize_money_email(self.team, self.prize_money)