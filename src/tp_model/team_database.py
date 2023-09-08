import os
import sqlite3
from tp_model import team_model, team_principal_staff_model

def add_teams(model):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")

	# GET COLUMN NAMES
	table_name = "teams"
	cursor = conn.execute(f'PRAGMA table_info({table_name})')
	columns = cursor.fetchall()
	column_names = [column[1] for column in columns]

	# GET COLUMN INDECES
	name_idx = column_names.index("Name")
	nation_idx = column_names.index("Nationality")
	speed_idx = column_names.index("car_speed")
	failure_idx = column_names.index("failure_probability")
	driver_1_idx = column_names.index("driver_1")
	driver_2_idx = column_names.index("driver_2")
	hq_idx = column_names.index("Headquarters")
	tp_idx = column_names.index("TP")
	workforce_idx = column_names.index("Workforce")

	# FACILITIES
	windtunnel_idx = column_names.index("Windtunnel")
	super_computer_idx = column_names.index("Super_Computer")
	engine_factory_idx = column_names.index("Engine Factory")
	chassis_workshop_idx = column_names.index("Chassis_Workshop")
	brake_center_idx = column_names.index("Brake Center")

	# STATS
	drivers_championships_idx = column_names.index("Drivers Championships")
	constructors_championships_idx = column_names.index("Constructors Championships")
	wins_idx = column_names.index("Wins")

	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM teams")
	teams = cursor.fetchall()

	for team in teams:
		name = team[name_idx]
		speed = team[speed_idx]
		nationality = team[nation_idx]
		car_failure_probability = team[failure_idx]
		hq = team[hq_idx]
		tp = model.get_team_principal_from_name(team[tp_idx])
		wind_tunnel = team[windtunnel_idx]
		super_computer = team[super_computer_idx]
		engine_factory = team[engine_factory_idx]
		chassis_workshop = team[chassis_workshop_idx]
		brake_center = team[brake_center_idx]
		workforce = team[workforce_idx]

		# Stats
		drivers_championships = team[drivers_championships_idx]
		constructors_championships = team[constructors_championships_idx]
		wins = team[wins_idx]

		model.teams.append(team_model.Team(model, name, speed, car_failure_probability, nationality, hq, tp,
									 drivers_championships, constructors_championships, wins,
									wind_tunnel, super_computer, engine_factory, chassis_workshop, brake_center,
									workforce))

		model.teams[-1].drivers = [team[driver_1_idx], team[driver_2_idx]]
		model.teams[-1].drivers_next_year = [team[driver_1_idx], team[driver_2_idx]]
		model.season.setup_initial_standings()

		for team in model.teams:
			team.set_drivers_team()
			team.drivers_next_year = team.drivers

def add_staff(model, year):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")

	# GET COLUMN NAMES
	table_name = "staff"
	cursor = conn.execute(f'PRAGMA table_info({table_name})')
	columns = cursor.fetchall()
	column_names = [column[1] for column in columns]

	# GET COLUMN INDECES
	name_idx = column_names.index("Name")
	role_idx = column_names.index("Role")

	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM staff WHERE Year_Appear = '{str(year)}'")
	staff = cursor.fetchall()

	for person in staff:
		name = person[name_idx]
		role = person[role_idx]

		if role == "TP":
			model.team_principals.append(team_principal_staff_model.TeamPrincipalStaff(name))