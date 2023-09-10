import random

class Car:
	def __init__(self, team, speed, car_failure_probability):
		self.team = team
		self.speed = speed
		self.failure_probability = car_failure_probability

		self.setup_variables()

	def setup_variables(self):
		self.speed_at_current_race = self.speed

		self.speed_tracker = []

	def update_car_speed(self):

		# Define weights for each facility
		wind_tunnel_weight = 0.2
		super_computer_weight = 0.1
		engine_factory_weight = 0.2
		chassis_workshop_weight = 0.1
		brake_center_weight = 0.1
		technical_director_weight = 0.2
		workforce_wight = 0.1

		workforce_factor = int(100 * (self.team.workforce/1000)) # generate number between 1 and 100 for workforce

		total_weighted_score = int(
            self.team.wind_tunnel * wind_tunnel_weight +
            self.team.super_computer * super_computer_weight +
            self.team.engine_factory * engine_factory_weight +
            self.team.chassis_workshop * chassis_workshop_weight +
            self.team.brake_center * brake_center_weight +
            self.team.technical_director.technical_knowledge * technical_director_weight +
            workforce_factor * workforce_wight
        )
		
		self.speed = total_weighted_score

		if self.speed > 70:
			self.speed = random.randint(70, 95)
		elif self.speed > 50:
			self.speed = random.randint(40, 75)
		else:
			self.speed = random.randint(30, 55)

		self.speed_tracker.append(self.speed)