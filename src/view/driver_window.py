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

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="Driver", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.main_frame = customtkinter.CTkFrame(self)
		self.main_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.stats_frame = customtkinter.CTkFrame(self)
		self.stats_frame.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		
		customtkinter.CTkLabel(self.stats_frame, text="Statistics", font=self.view.header1_font).grid(row=0,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")
		
		self.attributes_frame = customtkinter.CTkFrame(self)
		self.attributes_frame.grid(row=1, column=1, rowspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.attributes_frame, text="Attributes", font=self.view.header1_font).grid(row=0,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")
		
		# MAIN FRAME
		# self.image_label = Label(self.main_frame)
		# self.image_label.grid(row=1, column=1, rowspan=1, columnspan=16, sticky="NW")
		self.driver_image_label =  customtkinter.CTkLabel(self.main_frame, text="")
		self.driver_image_label.grid(row=1, column=1, rowspan=1, columnspan=16, sticky="NW")

		self.name_label = customtkinter.CTkLabel(self.main_frame, text="Name: Mr X", font=self.view.normal_font)
		self.name_label.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.nationality_label = customtkinter.CTkLabel(self.main_frame, text="Nationality: Irish", font=self.view.normal_font)
		self.nationality_label.grid(row=3, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.age_label = customtkinter.CTkLabel(self.main_frame, text="Age: 99", font=self.view.normal_font)
		self.age_label.grid(row=4, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		# STATS FRAME
		self.championships_label = customtkinter.CTkLabel(self.stats_frame, text="Championships: 0", font=self.view.normal_font)
		self.championships_label.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

		self.wins_label = customtkinter.CTkLabel(self.stats_frame, text="Wins: 0", font=self.view.normal_font)
		self.wins_label.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW") 

	def update_window(self, data):
		self.driver_image = customtkinter.CTkImage(light_image=self.view.driver_images[data["name"]], size=(400, 400))
		self.driver_image_label.configure(image=self.driver_image)
		
		self.name_label.configure(text=f'Name: {data["name"]}')
		self.nationality_label.configure(text=f'Nationality: {data["nationality"]}')
		self.age_label.configure(text=f'Age: {data["age"]}')
		self.championships_label.configure(text=f'Championships: {data["championships"]}')
		self.wins_label.configure(text=f'Wins: {data["wins"]}')
		
