import random

class TechnicalDirector:
	def __init__(self, name, age, technical_knowledge, resource_management):
		self.name = name
		self.age = age
		self.technical_knowledge = technical_knowledge
		self.resource_management = resource_management

		self.wants_to_move = False
		self.team = None

	def decide_switch_teams(self):

		random_value = random.random()

		if random_value < 0.1:
			self.wants_to_move = True
		else:
			self.wants_to_move = False

