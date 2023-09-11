

def technical_director_switch_teams_checks(model):
	check_all_teams_have_a_technical_director(model)
	check_technical_director_not_hired_by_two_teams(model)


def check_all_teams_have_a_technical_director(model):
	for team in model.teams:
		if team.technical_director is None:
			for t in model.technical_directors:
				print(f"{t.name} - {t.team}")
		assert team.technical_director is not None, f"{team.name} has no Technical Director"
		

def check_technical_director_not_hired_by_two_teams(model):
	tds = [t.technical_director for t in model.teams]
	if len(tds) != len(set(tds)):
		print([t.technical_director.name for t in model.teams])
		assert len(tds) == len(set(tds)), "A Technical Director is Hired by More than 1 Team"