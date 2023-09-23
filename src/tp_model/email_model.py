
from tp_model import email_generation


class Email:
	def __init__(self, subject, message):
		self.subject = subject
		self.message = message
		self.status = "unread"


class Inbox:
	def __init__(self, model):
		self.model = model
		self.emails = []
		self.new_mails = 0

	def add_email(self, email):
		self.emails.append(email)
		self.new_mails += 1

	def generate_driver_retirement_email(self, driver):
		msg = email_generation.driver_retirement(driver)
		email = Email(f"{driver.name} retiring!", msg)

		self.add_email(email)

	def generate_driver_hiring_email(self, team, driver):
		msg = email_generation.driver_hiring_email(team, driver)

		email = Email(f"{team.name} have hired {driver.name}!", msg)
		self.add_email(email)

	def generate_facility_update_email(self, team, facility):
		msg = email_generation.upgrade_facility(team, facility)

		email = Email(f"{team.name} have upgraded their {facility}!", msg)
		self.add_email(email)

	def new_technical_director_email(self, team, technical_director):
		msg = email_generation.hire_technical_director_email(team, technical_director)

		email = Email(f"New TD: {team.name} have hired {technical_director.name}!", msg)
		self.add_email(email)

	def new_sponsor_income_email(self, team):
		msg = email_generation.sponsor_income_update_email(team)

		email = Email(f"Sponsor Income Update", msg)
		self.add_email(email)

	def new_prize_money_email(self, team, prize_money):
		msg = email_generation.prize_money_email(team, prize_money)

		email = Email(f"Prize Money Confirmed", msg)
		self.add_email(email)