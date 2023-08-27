import random

class Car:
	def __init__(self, team, speed, car_failure_probability):
		self.team = team
		self.speed = speed
		self.failure_probability = car_failure_probability

		self.setup_variables()

	def setup_variables(self):
		self.speed_at_current_race = self.speed

	def update_car_speed(self):

		if self.speed > 70:
			self.speed = random.randint(70, 95)
		elif self.speed > 50:
			self.speed = random.randint(40, 75)
		else:
			self.speed = random.randint(30, 55)

	# def calculate_speed_at_current_race(self):
	# 	'''
	# 	This method is intended to give some variation of car speed at each track
	# 	Currently it is just a random variation of the baseline speed
	# 	'''

	# 	self.speed_at_current_race = self.speed
	# 	self.speed_at_current_race += random.randint(-5, 5)

	# 	if self.speed_at_current_race > 100:
	# 		self.speed_at_current_race = 100
	# 	elif self.speed_at_current_race <= 0:
	# 		self.speed_at_current_race = 1


		
