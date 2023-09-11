
from tp_model import email_generation


class Email:
	def __init__(self, subject, message):
		self.subject = subject
		self.message = message


class Inbox:
	def __init__(self, model):
		self.model = model
		self.emails = []


	def generate_driver_retirement_email(self, driver):
		msg = email_generation.driver_retirement(driver)
		email = Email(f"{driver.name} retiring!", msg)

		self.emails.append(email)

	def generate_driver_hiring_email(self, team, driver):
		msg = email_generation.driver_hiring_email(team, driver)

		email = Email(f"{team.name} have hired {driver.name}!", msg)
		self.emails.append(email)

	def generate_facility_update_email(self, team, facility):
		msg = email_generation.upgrade_facility(team, facility)

		email = Email(f"{team.name} have upgraded their {facility}!", msg)
		self.emails.append(email)

	def new_technical_director_email(self, team, technical_director):
		msg = email_generation.hire_technical_director_email(team, technical_director)

		email = Email(f"New TD: {team.name} have hired {technical_director.name}!", msg)
		self.emails.append(email)