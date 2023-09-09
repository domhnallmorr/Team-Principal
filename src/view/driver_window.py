import customtkinter
from tksheet import Sheet
from tkinter import *

class DriverWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(1, weight=1)		

		for i in range(4):
			self.stats_frame.grid_columnconfigure(i, weight=1)
		
		self.seasons_frame.grid_columnconfigure(1, weight=1)

	def setup_widgets(self):
		self.title_label = customtkinter.CTkLabel(self, text="Driver", font=self.view.page_title_font)
		self.title_label.grid(row=0, column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.main_frame = customtkinter.CTkFrame(self)
		self.main_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.stats_frame = customtkinter.CTkFrame(self)
		self.stats_frame.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		
		customtkinter.CTkLabel(self.stats_frame, text="Statistics", font=self.view.header1_font).grid(row=0,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.seasons_frame = customtkinter.CTkFrame(self)
		self.seasons_frame.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		
		customtkinter.CTkLabel(self.seasons_frame, text="Previous Seasons", font=self.view.header1_font).grid(row=0,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")
			
		self.attributes_frame = customtkinter.CTkFrame(self)
		self.attributes_frame.grid(row=1, column=1, rowspan=3, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.attributes_frame, text="Attributes", font=self.view.header1_font).grid(row=0,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")
		
		# MAIN FRAME
		self.driver_image_label =  customtkinter.CTkLabel(self.main_frame, text="")
		self.driver_image_label.grid(row=1, column=1, rowspan=16, columnspan=1, sticky="NW")

		self.age_label = customtkinter.CTkLabel(self.main_frame, text="Age: 99", font=self.view.normal_font)
		self.age_label.grid(row=1, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.nationality_label = customtkinter.CTkLabel(self.main_frame, text="Nationality: Irish", font=self.view.normal_font)
		self.nationality_label.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.hometown_label = customtkinter.CTkLabel(self.main_frame, text="Hometown: Cashel", font=self.view.normal_font)
		self.hometown_label.grid(row=3, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.team_label = customtkinter.CTkLabel(self.main_frame, text="Team: Morrissey", font=self.view.normal_font)
		self.team_label.grid(row=4, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		# STATS FRAME
		self.championships_label = customtkinter.CTkLabel(self.stats_frame, text="Championships: 0", font=self.view.normal_font)
		self.championships_label.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.races_label = customtkinter.CTkLabel(self.stats_frame, text="Races: 0", font=self.view.normal_font)
		self.races_label.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.wins_label = customtkinter.CTkLabel(self.stats_frame, text="Wins: 0", font=self.view.normal_font)
		self.wins_label.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.podiums_label = customtkinter.CTkLabel(self.stats_frame, text="Podiums: 0", font=self.view.normal_font)
		self.podiums_label.grid(row=2, column=3, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		# Seasons Frame
		self.seasons_sheet = self.view.setup_tksheet_table(self.seasons_frame, ["Year", "Races", "Wins", "Podiums", "Points", "DNFs", "Pos."])
		self.seasons_sheet.grid(row=1, column=0, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW") 
		self.seasons_sheet.set_options(auto_resize_columns=50)

	def update_window(self, data):
		self.driver_image = customtkinter.CTkImage(light_image=self.view.driver_images[data["name"]], size=(400, 400))
		self.driver_image_label.configure(image=self.driver_image)
		
		self.title_label.configure(text=f'{data["name"]}')
		self.nationality_label.configure(text=f'Nationality: {data["nationality"]}')
		self.hometown_label.configure(text=f'Hometown: {data["hometown"]}')
		self.age_label.configure(text=f'Age: {data["age"]}')
		self.team_label.configure(text=f'Team: {data["team"]}')
		
		# Stats
		self.championships_label.configure(text=f'Championships: {data["championships"]}')
		self.wins_label.configure(text=f'Wins: {data["wins"]}')
		self.races_label.configure(text=f'Races: {data["races"]}')
		self.podiums_label.configure(text=f'Podiums: {data["podiums"]}')
		
		# Seasons
		self.view.update_tksheet_table(self.seasons_sheet, data["seasons_data"])
