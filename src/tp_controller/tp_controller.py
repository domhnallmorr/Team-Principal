from tp_model import tp_model, update_window_functions
from view import view

class TPController:
	def __init__(self, app):
		self.app = app

		self.model = tp_model.TPModel()
		self.view = view.View(self)
		self.view.setup_track_maps(self.model.tracks)
		self.setup_driver_images()

		self.update_main_window()
		self.update_calender_window()
		self.update_standings_window()

	def setup_driver_images(self):
		driver_image_data = self.model.get_driver_image_data()
		self.view.setup_driver_images(driver_image_data)

	def update_main_window(self):
		data = update_window_functions.get_main_window_data(self.model)
		self.view.main_window.update_window(data)

	def update_calender_window(self):
		data = self.model.get_calender_window_data()
		self.view.calender_window.update_window(data)

	def update_email_window(self):
		data = update_window_functions.update_email_window(self.model)
		self.view.email_window.update_window(data)

	def update_standings_window(self):
		data = self.model.get_standings_window_data()
		self.view.standings_window.update_window(data)

	def update_race_weekend_window(self):
		data = self.model.get_race_weekend_data()
		self.view.race_weekend_window.update_window(data)

	def show_driver_window(self, driver):
		data = self.model.get_driver_window_data(driver)
		self.view.driver_window.update_window(data)
		self.view.change_window("driver")

	def show_circuit_window(self, track):
		data = self.model.get_circuit_window_data(track)
		self.view.circuit_window.update_window(data)
		self.view.change_window("circuit")

	def advance(self):
		is_new_season = self.model.advance()
		self.update_main_window()
		self.update_standings_window()
		self.update_email_window()

		if is_new_season is True:
			self.setup_driver_images() # ensure any new drivers images are generated for the view

	def go_to_race(self):
		self.view.change_window("main_race")

		self.model.simulate_race()
		
		self.view.change_window("main")
		self.view.change_window("results")

		data = self.model.get_results_window_data()
		self.view.results_window.update_window(data)

		self.update_standings_window()
		self.update_main_window()
		
		self.view.main_window.update_advance_btn("advance")

