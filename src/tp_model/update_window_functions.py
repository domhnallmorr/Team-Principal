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

def get_circuit_window_data(model, track):
	data = {}

	data["name"] = track
	track = model.get_instance_by_name(track, "Track")
	data["description"] = track.description
	data["city"] = track.city
	data["country"] = track.country
	data["length"] = round(track.length/1000, 3)
	data["laps"] = track.no_of_laps

	data["downforce"] = track.downforce
	data["grip"] = track.grip
	data["top_speed"] = track.top_speed
	data["braking"] = track.braking
	
	return data

def get_driver_window_data(model, driver):
	data = {}

	data["name"] = driver
	driver = model.get_instance_by_name(driver, "Driver")
	data["age"] = driver.age
	data["nationality"] = driver.nationality
	data["hometown"] = driver.hometown

	if driver.team is not None:
		data["team"] = driver.team.name
	else:
		data["team"] = "N/A"
		
	data["championships"] = driver.championships
	data["wins"] = driver.wins
	data["races"] = driver.races
	data["podiums"] = driver.podiums
	data["seasons_data"] = driver.season_stats_df.values.tolist()

	return data

def get_team_window_data(model, team):
	data = {}

	data["name"] = team
	team = model.get_instance_by_name(team, "Team")
	data["nationality"] = team.nationality
	data["headquarters"] = team.headquarters
	data["tp"] = team.team_principal.name
	data["technical_director"] = team.technical_director.name
	data["wind_tunnel"] = team.wind_tunnel
	data["super_computer"] = team.super_computer
	data["engine_factory"] = team.engine_factory
	data["chassis_workshop"] = team.chassis_workshop
	data["brake_center"] = team.brake_center
	data["workforce"] = team.workforce
	data["driver_1"] = team.drivers[0]
	data["driver_2"] = team.drivers[1]

	data["drivers_championships"] = team.drivers_championships
	data["constructors_championships"] = team.constructors_championships
	data["wins"] = team.wins

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

def get_standings_window_data(model):
	data = {}
	data["driver_standings"] = model.season.driver_standings
	data["team_standings"] = model.season.team_standings

	return data