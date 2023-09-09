import customtkinter
from tksheet import Sheet
from tkinter import *

class TeamWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(2, weight=1)		

		self.driver_frame.grid_columnconfigure(0, weight=1)
		self.driver_frame.grid_columnconfigure(1, weight=1)

		self.stats_frame.grid_columnconfigure(0, weight=1)
		self.stats_frame.grid_columnconfigure(1, weight=1)
		self.stats_frame.grid_columnconfigure(2, weight=1)

	def setup_widgets(self):
		self.title_label = customtkinter.CTkLabel(self, text="Team", font=self.view.page_title_font)
		self.title_label.grid(row=0, column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.main_frame = customtkinter.CTkFrame(self)
		self.main_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.driver_frame = customtkinter.CTkFrame(self)
		self.driver_frame.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.stats_frame = customtkinter.CTkFrame(self)
		self.stats_frame.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.facilities_frame = customtkinter.CTkFrame(self)
		self.facilities_frame.grid(row=1, column=1, rowspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.facilities_frame, text="Facilities", font=self.view.header1_font).grid(row=0,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")
		# MAIN FRAME
		self.nationality_label = customtkinter.CTkLabel(self.main_frame, text="Nationality: Irish", font=self.view.normal_font)
		self.nationality_label.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.hq_label = customtkinter.CTkLabel(self.main_frame, text="Headquarters: Somewhere", font=self.view.normal_font)
		self.hq_label.grid(row=3, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.tp_label = customtkinter.CTkLabel(self.main_frame, text="Team Principal: Someone", font=self.view.normal_font)
		self.tp_label.grid(row=4, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.td_label = customtkinter.CTkLabel(self.main_frame, text="Technical Director: Someone", font=self.view.normal_font)
		self.td_label.grid(row=5, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.workforce_label = customtkinter.CTkLabel(self.main_frame, text="Workforce: 500", font=self.view.normal_font)
		self.workforce_label.grid(row=6, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		# DRIVER FRAME
		customtkinter.CTkLabel(self.driver_frame, text="Drivers", font=self.view.header1_font).grid(row=0,
										     column=0, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.driver_1_image_label =  customtkinter.CTkLabel(self.driver_frame, text="")
		self.driver_1_image_label.grid(row=1, column=0, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.driver_1_label = customtkinter.CTkLabel(self.driver_frame, text="Name:", font=self.view.normal_font)
		self.driver_1_label.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.driver_2_image_label =  customtkinter.CTkLabel(self.driver_frame, text="")
		self.driver_2_image_label.grid(row=1, column=1, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.driver_2_label = customtkinter.CTkLabel(self.driver_frame, text="Name:", font=self.view.normal_font)
		self.driver_2_label.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		# DRIVER FRAME
		customtkinter.CTkLabel(self.stats_frame, text="Statistics", font=self.view.header1_font).grid(row=0,
										     column=0, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.drivers_championships_label =  customtkinter.CTkLabel(self.stats_frame, text="Drivers Championships:", anchor="w", font=self.view.normal_font)
		self.drivers_championships_label.grid(row=1, column=0, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.contructors_championships_label =  customtkinter.CTkLabel(self.stats_frame, text="Constructors Championships:", anchor="w", font=self.view.normal_font)
		self.contructors_championships_label.grid(row=1, column=1, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.wins_label =  customtkinter.CTkLabel(self.stats_frame, text="Wins:", anchor="w", font=self.view.normal_font)
		self.wins_label.grid(row=1, column=2, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")


		# FACILITIES FRAME
		customtkinter.CTkLabel(self.facilities_frame, text="Wind Tunnel:", anchor="w", font=self.view.normal_font).grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.wind_tunnel_progressbar = customtkinter.CTkProgressBar(self.facilities_frame, orientation="horizontal")
		self.wind_tunnel_progressbar.grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.facilities_frame, text="Super Computer:", anchor="w", font=self.view.normal_font).grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.super_computer_progressbar = customtkinter.CTkProgressBar(self.facilities_frame, orientation="horizontal")
		self.super_computer_progressbar.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.facilities_frame, text="Engine Factory:", anchor="w", font=self.view.normal_font).grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.engine_factory_progressbar = customtkinter.CTkProgressBar(self.facilities_frame, orientation="horizontal")
		self.engine_factory_progressbar.grid(row=3, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.facilities_frame, text="Chassis Workshop:", anchor="w", font=self.view.normal_font).grid(row=4, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.chassis_workshop_progressbar = customtkinter.CTkProgressBar(self.facilities_frame, orientation="horizontal")
		self.chassis_workshop_progressbar.grid(row=4, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.facilities_frame, text="Brake Center:", anchor="w", font=self.view.normal_font).grid(row=5, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.brake_center_progressbar = customtkinter.CTkProgressBar(self.facilities_frame, orientation="horizontal")
		self.brake_center_progressbar.grid(row=5, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

	def update_window(self, data):	
		self.title_label.configure(text=f'{data["name"]}')
		self.nationality_label.configure(text=f'Nationality: {data["nationality"]}')
		self.hq_label.configure(text=f'Headquarters: {data["headquarters"]}')
		self.tp_label.configure(text=f'Team Principal: {data["tp"]}')
		self.td_label.configure(text=f'Technical Director: {data["technical_director"]}')
		self.workforce_label.configure(text=f'Workforce: {data["workforce"]}')

		# Drivers
		self.driver_1_image = customtkinter.CTkImage(light_image=self.view.driver_images[data["driver_1"]], size=(200, 200))
		self.driver_1_image_label.configure(image=self.driver_1_image)

		self.driver_1_label.configure(text=f'Name: {data["driver_1"]}')

		self.driver_2_image = customtkinter.CTkImage(light_image=self.view.driver_images[data["driver_2"]], size=(200, 200))
		self.driver_2_image_label.configure(image=self.driver_2_image)

		self.driver_2_label.configure(text=f'Name: {data["driver_2"]}')

		# STATS
		self.drivers_championships_label.configure(text=f"Drivers Championships: {data['drivers_championships']}")
		self.contructors_championships_label.configure(text=f"Constructors Championships: {data['constructors_championships']}")
		self.wins_label.configure(text=f"Wins: {data['wins']}")

		# FACILITIES
		self.wind_tunnel_progressbar.set(data["wind_tunnel"]/100)
		self.super_computer_progressbar.set(data["super_computer"]/100)
		self.engine_factory_progressbar.set(data["engine_factory"]/100)
		self.chassis_workshop_progressbar.set(data["chassis_workshop"]/100)
		self.brake_center_progressbar.set(data["brake_center"]/100)