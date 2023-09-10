import pickle
import matplotlib.pyplot as plt
from tp_model import tp_model

def run_model():
	model = tp_model.TPModel(mode="headless")
	
	while model.season.year < 2010:
			
		model.advance()

	for team in model.teams:
		plt.plot([i for i in range(len(team.car.speed_tracker))], team.car.speed_tracker, label=team.name)
	
	plt.legend()
	plt.grid()
	plt.show()

if __name__ == "__main__":
	run_model()