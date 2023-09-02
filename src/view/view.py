import copy

from tkinter import *
from view import main_window, calender_window, circuit_window, driver_window, main_race_window, standings_window, race_weekend_window, results_window
from view import email_window, tp_icons
from tkinter import font as tkfont

from tksheet import Sheet

class View:
	def __init__(self, controller, default_year):
		self.controller = controller

		self.pady = 5
		self.padx = 7
		self.padx_large = 25 # if a large gap is needed

		self.success_color = "#33871C"
		self.success_color_darker = "#194F0A"

		self.page_title_font = ("Verdana", 30)
		self.header1_font = ("Verdana", 24)
		self.header2_font = ("Verdana", 19)
		self.normal_font = ("Verdana", 15)

		self.tksheet_normal_font = ("Verdana", 12, "normal")

		tp_icons.setup_icons(self)
		self.setup_windows(default_year)

		self.track_maps = {}

	def setup_windows(self, default_year):
		self.main_window = main_window.MainWindow(self.controller.app, self)
		self.main_window.pack(expand=True, fill=BOTH, side=LEFT)

		self.calender_window = calender_window.CalenderWindow(self.main_window.page_frame, self, default_year)
		self.calender_window.grid(row=0, column=0, sticky="NSEW")
		self.current_window = self.calender_window

		self.email_window = email_window.EmailWindow(self.main_window.page_frame, self)
		self.circuit_window = circuit_window.CircuitWindow(self.main_window.page_frame, self)
		self.driver_window = driver_window.DriverWindow(self.main_window.page_frame, self)
		self.standings_window = standings_window.StandingsWindow(self.main_window.page_frame, self)
		self.race_weekend_window = race_weekend_window.RaceWeekendWindow(self.main_window.page_frame, self)
		self.results_window = results_window.ResultsWindow(self.main_window.page_frame, self)
		
		self.main_race_window = main_race_window.MainRaceWindow(self.controller.app, self)
		
		
	def change_window(self, window):
		self.current_window.grid_forget()

		if window == "calender":
			self.calender_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.calender_window

		elif window == "circuit":
			self.circuit_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.circuit_window

		elif window == "driver":
			self.driver_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.driver_window

		elif window == "email":
			self.email_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.email_window

		elif window == "standings":
			self.standings_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.standings_window

		elif window == "race_weekend":
			self.controller.update_race_weekend_window()
			self.race_weekend_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.race_weekend_window

		elif window == "main_race":
			self.main_window.pack_forget()
			self.main_race_window.pack(expand=True, fill=BOTH, side=LEFT)

		elif window == "main":
			self.main_race_window.pack_forget()
			self.main_window.pack(expand=True, fill=BOTH, side=LEFT)

		elif window == "results":
			self.results_window.grid(row=0, column=0, sticky="NSEW")
			self.current_window = self.results_window

	def setup_tksheet_table(self, parent, headers):
		return Sheet(parent, headers=headers, font=self.tksheet_normal_font, column_width=300, show_x_scrollbar=False,
				      					frame_bg="#333333", table_bg="#333333", table_fg="#ffffff", header_bg="#333333", header_fg="#ffffff",
										index_bg="#333333", index_fg="#ffffff", top_left_bg="#333333",
										header_font=self.tksheet_normal_font,
										index_font=self.tksheet_normal_font,
										)

	def update_tksheet_table(self, table, data):

		table.set_sheet_data(data=data,
               reset_col_positions=False,
               reset_row_positions=True,
               redraw=True,
               verify=False,
               reset_highlights=False)


	def setup_driver_images(self, data):
		tp_icons.setup_driver_images(self, data)
		
	def setup_track_maps(self, tracks):
		for track in tracks:
			tp_icons.create_track_map(self, track.name, track.track_map)