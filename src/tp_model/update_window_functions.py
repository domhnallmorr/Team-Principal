import copy

def get_main_window_data(model):
	data = {}

	if model.season.current_round != "off_season":
		data["date"] = f"Week {model.season.current_week} - Next Race: {model.season.year}\t{model.season.get_next_race_text()}"
	else:
		data["date"] = f"Week {model.season.current_week} - Off Season {model.season.year}"
	data["in_race_week"] = model.in_race_week

	return data

def get_calender_window_data(model, year):
	data = {}

	data["year"] = year
	data["years"] = [str(y) for y in list(model.season.previous_results.keys())]
	data["calender"] = copy.deepcopy(model.season.calender)

	# Add winners
	for idx, race in enumerate(data["calender"]):
		data["calender"][idx].append("-")

		if len(model.season.previous_results[year][idx]) == 6:
			race_winner = model.season.previous_results[year][idx][-1][0][0]
			data["calender"][idx][-1] = race_winner

	return data
	
def update_email_window(model):
	data = {}

	data["emails"] = []

	for email in reversed(model.inbox.emails):
		data["emails"].append([email.subject, email.message])

	return data

def get_previous_result(model, year, race_idx):
		data = {}
		if len(model.season.previous_results[year][race_idx]) == 5:
			result = None # race has not been run yet
		else:
			result = model.season.previous_results[year][race_idx][-1]
		data["results"] = result
  
		data["race_title"] = f"{model.season.previous_results[year][race_idx][1]} - {year}"

		return data