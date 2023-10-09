import copy
import random

def get_available_commercial_managers(model):

	commercial_managers = copy.deepcopy(model.commercial_managers)

	return commercial_managers


class CommercialManager:
	def __init__(self, name, age, negotiation_skill, reputation):
		self.name = name
		self.age = age
		self.negotiation_skill = negotiation_skill
		self.reputation = reputation

		self.wants_to_move = False
		self.team = None

	def decide_switch_teams(self):

		random_value = random.random()

		if random_value < 0.1:
			self.wants_to_move = True
		else:
			self.wants_to_move = False


	def negotiate_new_deal(self):

        # Calculate the sponsorship income based on negotiation skill with a random component
		multiplier = 700_000     # Adjust this value based on your game balance
		bias = self.negotiation_skill/100
		income = self.negotiation_skill * multiplier * bias

        # Add a random element to the income calculation
		random_percentage = random.uniform(0.8, 1.2)  # Random value between 0.9 and 1.1 (adjust as needed)
		income *= random_percentage

		return int(income)
	
if __name__ == "__main__":
	c = CommercialManager("name", 1, 90, 100)

	for i in range(10):
		print(f"{c.negotiate_new_deal():,}")

