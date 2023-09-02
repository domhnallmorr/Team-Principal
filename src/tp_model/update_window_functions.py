

def get_main_window_data(model):
	data = {}

	if model.season.current_round != "off_season":
		data["date"] = f"Week {model.season.current_week} - Next Race: {model.season.year}\t{model.season.get_next_race_text()}"
	else:
		data["date"] = f"Week {model.season.current_week} - Off Season {model.season.year}"
	data["in_race_week"] = model.in_race_week

	return data

def update_email_window(model):
	data = {}

	data["emails"] = []

	for email in reversed(model.inbox.emails):
		data["emails"].append([email.subject, email.message])

	return data