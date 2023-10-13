from tp_model import tp_model, update_window_functions
from view import view, hire_commercial_manager_window, upgrade_facilities_window

import tkinter as tk

class TPController:
	def __init__(self, app):
		self.app = app

		self.model = tp_model.TPModel()
		self.view = view.View(self, self.model.season.year)
		self.view.setup_track_maps(self.model.tracks)
		self.setup_driver_images()

		self.update_all_windows()

	def setup_driver_images(self):
		driver_image_data = self.model.get_driver_image_data()
		self.view.setup_driver_images(driver_image_data)

	def update_main_window(self):
		data = update_window_functions.get_main_window_data(self.model)
		self.view.main_window.update_window(data)

	def update_calender_window(self, year):
		data = update_window_functions.get_calender_window_data(self.model, year)
		self.view.calender_window.update_window(data)

	def update_car_window(self):
		data = update_window_functions.get_car_window_data(self.model)
		self.view.car_window.update_window(data)

	def update_email_window(self):
		data = update_window_functions.update_email_window(self.model)
		self.view.email_window.update_window(data)

	def update_finance_window(self):
		data = update_window_functions.update_finance_window(self.model)
		self.view.finance_summary_window.update_window(data)
		self.view.income_window.update_window(data)
		self.view.expenditure_window.update_window(data)

	def update_sponsors_window(self):
		data = update_window_functions.get_sponsors_window_data(self.model)
		self.view.sponsors_window.update_window(data)

	def update_standings_window(self):
		data = update_window_functions.get_standings_window_data(self.model)
		self.view.standings_window.update_window(data)

	def update_race_weekend_window(self):
		data = self.model.get_race_weekend_data()
		self.view.race_weekend_window.update_window(data)

	def show_driver_window(self, driver):
		data = update_window_functions.get_driver_window_data(self.model, driver)
		self.view.driver_window.update_window(data)
		self.view.change_window("driver")

	def show_team_window(self, team):
		data = update_window_functions.get_team_window_data(self.model, team)
		self.view.team_window.update_window(data)
		self.view.change_window("team")

	def show_circuit_window(self, track):
		data = update_window_functions.get_circuit_window_data(self.model, track)
		self.view.circuit_window.update_window(data)
		self.view.change_window("circuit")

	def update_all_windows(self):
		self.update_main_window()
		self.update_calender_window(self.model.season.year)
		self.update_standings_window()
		self.update_sponsors_window()
		self.update_finance_window()
		self.update_car_window()
		self.update_sponsors_window()

	def advance(self):
		is_new_season = self.model.advance()
		self.update_main_window()
		self.update_standings_window()
		self.update_email_window()
		self.update_finance_window()
		self.update_calender_window(self.model.season.year)
		self.update_sponsors_window()

		if is_new_season is True:
			self.setup_driver_images() # ensure any new drivers images are generated for the view

	def go_to_race(self):
		self.view.change_window("main_race")

		self.model.simulate_race()
		
		self.view.change_window("main")

		if self.model.season.current_round == "off_season":
			race_idx = -1
		else:
			race_idx = self.model.season.current_round - 1

		self.show_race_result(self.model.season.year, race_idx)

		self.update_standings_window()
		self.update_main_window()
		self.update_calender_window(self.model.season.year)
		self.update_email_window()
		
		self.view.main_window.update_advance_btn("advance")

	def show_race_result(self, year, race_idx):
		data = update_window_functions.get_previous_result(self.model, year, race_idx)
		if data["results"] is not None:
			self.view.results_window.update_window(data)
			self.view.change_window("results")

	def show_player_team_page(self):
		self.show_team_window(self.model.player_team.name)

	def hire_commercial_manager(self):
		if self.model.player_team.commercial_manager_next_year is not None:
			title="Position Already Filled"
			msg = "A Commercial Manager for Next Season Has Been Hired"
			self.view.show_warning_message(title, msg)
		else:
		
			data = update_window_functions.get_hire_commercial_manager_data(self.model)
			
			hired_manager = hire_commercial_manager_window.launch_window(self, data)

			if hired_manager is not None:
				self.model.player_team.commercial_manager_next_year = hired_manager

				title = "Successfully Hire"
				msg = f"{hired_manager.name} Will Join the Team at the Start of Next Season!"
				self.view.show_success_message(title, msg)
		
	def upgrade_facility(self):

		data = upgrade_facilities_window.launch_window(self, None)

		if data is not None:
			self.model.player_team.upgrade_player_facility(data)

			# UPDATE VIEW
			self.show_player_team_page()
			self.update_main_window()

			# SHOW POP UP
			title = "Upgrade Successfull"
			msg = f"{data['facility']} Upgraded Successfully"
			self.view.show_success_message(title, msg)
