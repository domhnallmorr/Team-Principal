
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