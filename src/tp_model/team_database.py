import os
import sqlite3
from tp_model import commercial_manager_model, team_model, team_principal_staff_model, technical_director_model

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
	technical_director_idx = column_names.index("Technical_Director")
	commercial_manager_idx = column_names.index("Commercial_Manager")
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
		tp = model.get_instance_by_name(team[tp_idx], "TeamPrincipal")
		technical_director = model.get_instance_by_name(team[technical_director_idx], "TechnicalDirector")
		commercial_manager = model.get_instance_by_name(team[commercial_manager_idx], "commercialManager")

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
									 technical_director, drivers_championships, constructors_championships, wins,
									wind_tunnel, super_computer, engine_factory, chassis_workshop, brake_center,
									workforce, commercial_manager))

		model.teams[-1].drivers = [team[driver_1_idx], team[driver_2_idx]]
		model.teams[-1].drivers_next_year = [team[driver_1_idx], team[driver_2_idx]]
		model.season.setup_initial_standings()

		for team in model.teams:
			team.set_drivers_team()
			team.drivers_next_year = team.drivers

def add_team_principals(model, year):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")

	# GET COLUMN NAMES
	table_name = "team_principals"
	cursor = conn.execute(f'PRAGMA table_info({table_name})')
	columns = cursor.fetchall()
	column_names = [column[1] for column in columns]

	# GET COLUMN INDECES
	name_idx = column_names.index("Name")
	role_idx = column_names.index("Role")

	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM team_principals WHERE Year_Appear = '{str(year)}'")
	staff = cursor.fetchall()

	for person in staff:
		name = person[name_idx]
		role = person[role_idx]

		if role == "TP":
			model.team_principals.append(team_principal_staff_model.TeamPrincipalStaff(name))

def add_technical_directors(model, year):

	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")

	# GET COLUMN NAMES
	table_name = "technical_directors"
	cursor = conn.execute(f'PRAGMA table_info({table_name})')
	columns = cursor.fetchall()
	column_names = [column[1] for column in columns]

	# GET COLUMN INDECES
	name_idx = column_names.index("Name")
	age_idx = column_names.index("Age")
	technical_knowledge_idx = column_names.index("Technical_Knowledge")
	resource_management_idx = column_names.index("Resource_Management")

	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM technical_directors WHERE Year_Appear = '{str(year)}'")
	staff = cursor.fetchall()

	for person in staff:
		name = person[name_idx]
		age = person[age_idx]
		technical_knowledge = person[technical_knowledge_idx]
		resource_management = person[resource_management_idx]

		model.technical_directors.append(technical_director_model.TechnicalDirector(name, age, technical_knowledge, resource_management))

def add_commercial_maangers(model, year):
	conn = sqlite3.connect(f"{os.getcwd()}\\tp_model\\team_principal.db")

	# GET COLUMN NAMES
	table_name = "commercial_managers"
	cursor = conn.execute(f'PRAGMA table_info({table_name})')
	columns = cursor.fetchall()
	column_names = [column[1] for column in columns]

	# GET COLUMN INDECES
	name_idx = column_names.index("Name")
	age_idx = column_names.index("Age")
	negotiation_skill_idx = column_names.index("Negotiation_skill")
	reputation_idx = column_names.index("Reputation")

	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM commercial_managers WHERE Year_Appear = '{str(year)}'")
	staff = cursor.fetchall()

	for person in staff:
		name = person[name_idx]
		age = person[age_idx]
		negotiation_skill = person[negotiation_skill_idx]
		reputation = person[reputation_idx]

		model.commercial_managers.append(commercial_manager_model.CommercialManager(name, age, negotiation_skill, reputation))
