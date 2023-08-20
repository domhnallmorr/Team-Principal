from PIL import ImageTk
import PIL.Image
import base64
import io
from tkinter import *

import customtkinter
from tksheet import Sheet


class RaceWeekendWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view
		self.setup_icons()
		self.setup_frames()

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=2)
		# self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(1, weight=1)		

		self.session_frame.grid_columnconfigure(0, weight=2)

		self.session_frame.grid_rowconfigure(1, weight=1)
		self.session_frame.grid_rowconfigure(2, weight=1)
		self.session_frame.grid_rowconfigure(3, weight=1)
		self.session_frame.grid_rowconfigure(4, weight=1)
		self.session_frame.grid_rowconfigure(5, weight=1)

		self.friday_practice_frame.grid_columnconfigure(2, weight=1)

	def setup_icons(self):
		self.sunny_icon = customtkinter.CTkImage(light_image=self.view.sunny_icon2, size=(50, 50))
		self.cloudy_icon = customtkinter.CTkImage(light_image=self.view.cloudy_icon2, size=(50, 50))

	def setup_frames(self):
		self.session_frame = customtkinter.CTkFrame(self)
		self.session_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.track_frame = customtkinter.CTkFrame(self)
		self.track_frame.grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
	
		self.friday_practice_frame = customtkinter.CTkFrame(self.session_frame)
		self.friday_practice_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.saturday_practice_frame = customtkinter.CTkFrame(self.session_frame)
		self.saturday_practice_frame.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.qualifying_frame = customtkinter.CTkFrame(self.session_frame)
		self.qualifying_frame.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.warmup_frame = customtkinter.CTkFrame(self.session_frame)
		self.warmup_frame.grid(row=4, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.race_frame = customtkinter.CTkFrame(self.session_frame)
		self.race_frame.grid(row=5, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="RACE WEEKEND", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		# FRIDAY ------------------------------
		customtkinter.CTkLabel(self.friday_practice_frame, text="Friday Practice", font=self.view.header1_font).grid(row=1,
										column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.friday_forecast_label = customtkinter.CTkLabel(self.friday_practice_frame, text="Forecast: 20°c  ", font=self.view.normal_font,
						      image=self.sunny_icon, compound=RIGHT)
		self.friday_forecast_label.grid(row=2, column=0, padx=(self.view.padx_large, self.view.padx), pady=self.view.pady, sticky="W")

		# dummy for grid
		customtkinter.CTkLabel(self.friday_practice_frame, text="", font=self.view.normal_font).grid(row=2, column=2, padx=self.view.padx_large, pady=self.view.pady, sticky="W")

		# SATURDAY ------------------------------
		customtkinter.CTkLabel(self.saturday_practice_frame, text="Saturday Practice", font=self.view.header1_font).grid(row=1,
										column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.saturday_forecast_label = customtkinter.CTkLabel(self.saturday_practice_frame, text="Forecast: 18°c  ", font=self.view.normal_font,
							image=self.sunny_icon, compound=RIGHT)
		self.saturday_forecast_label.grid(row=2, column=0, padx=(self.view.padx_large, self.view.padx), pady=self.view.pady, sticky="W")

		# QUALFYING ------------------------------
		customtkinter.CTkLabel(self.qualifying_frame, text="Qualfying", font=self.view.header1_font).grid(row=1,
										column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.qualy_forecast_label = customtkinter.CTkLabel(self.qualifying_frame, text="Forecast: 25°c  ", font=self.view.normal_font,
						     image=self.sunny_icon, compound=RIGHT)
		self.qualy_forecast_label.grid(row=2, column=0, padx=(self.view.padx_large, self.view.padx), pady=self.view.pady, sticky="W")

		# WARMUP ------------------------------
		customtkinter.CTkLabel(self.warmup_frame, text="Warmup", font=self.view.header1_font).grid(row=1,
										column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.warmup_forecast_label = customtkinter.CTkLabel(self.warmup_frame, text="Forecast: 17°c  ", font=self.view.normal_font,
						      image=self.cloudy_icon, compound=RIGHT)
		self.warmup_forecast_label.grid(row=2, column=0, padx=(self.view.padx_large, self.view.padx), pady=self.view.pady, sticky="W")

		# RACE ------------------------------
		customtkinter.CTkLabel(self.race_frame, text="Race", font=self.view.header1_font).grid(row=1,
										column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.race_forecast_label = customtkinter.CTkLabel(self.race_frame, text="Forecast: 27°c  ", font=self.view.normal_font,
						     image=self.cloudy_icon, compound=RIGHT)
		self.race_forecast_label.grid(row=2, column=0, padx=(self.view.padx_large, self.view.padx), pady=self.view.pady, sticky="NW")

		self.go_to_race_btn = customtkinter.CTkButton(self.race_frame, text="Go To Race", command=self.view.controller.go_to_race)
		self.go_to_race_btn.grid(row=10, column=0, padx=self.view.padx_large, pady=self.view.pady, sticky="NW")

		# Dummy label for grid configure
		# customtkinter.CTkLabel(self, text="", font=self.view.header1_font).grid(row=17,
		# 								column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.track_map_image_label =  customtkinter.CTkLabel(self.track_frame, text="")
		self.track_map_image_label.grid(row=1, column=1, rowspan=16, sticky="NW")

		# TRACK LABELS
		self.track_name_label = customtkinter.CTkLabel(self.track_frame, text="Track Name: Alexandra Park", font=self.view.normal_font)
		self.track_name_label.grid(row=19, column=1, padx=self.view.padx_large, pady=self.view.pady, sticky="NW")

		self.track_length_label = customtkinter.CTkLabel(self.track_frame, text="Track Length: 5.303 km", font=self.view.normal_font)
		self.track_length_label.grid(row=20, column=1, padx=self.view.padx_large, pady=self.view.pady, sticky="NW")

		self.number_of_laps_label = customtkinter.CTkLabel(self.track_frame, text="Laps: 58", font=self.view.normal_font)
		self.number_of_laps_label.grid(row=21, column=1, padx=self.view.padx_large, pady=self.view.pady, sticky="NW")

	def update_window(self, data):
		self.track_name_label.configure(text=f"Track Name: {data['name']}")
		self.track_length_label.configure(text=f"Track Length: {data['length']}")
		self.number_of_laps_label.configure(text=f"Laps: {data['laps']}")

		self.track_image = customtkinter.CTkImage(light_image=self.view.track_maps[data["name"]], size=(384, 192))
		self.track_map_image_label.configure(image=self.track_image)
		




