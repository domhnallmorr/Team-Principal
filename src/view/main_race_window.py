
import customtkinter
from tksheet import Sheet


class MainRaceWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(15, weight=1)
		self.grid_rowconfigure(5, weight=1)

	def setup_widgets(self):
		
		# LAP COUNTER
		self.lap_counter = customtkinter.CTkLabel(master=self, text="Lap:")
		self.lap_counter.grid(row=4, column=0, pady=self.view.pady, sticky="NSEW")

		# BUTTONS
		self.start_pause_btn = customtkinter.CTkButton(master=self, text="Start", command=self.start_pause)
		self.start_pause_btn.grid(row=6, column=0, pady=self.view.pady, sticky="NSEW")

		# TIMING SCREEN
		self.timing_headers = ["POS", "#", "NAME", "GAP", "INT", "LAPTIME", "RACE_TIME"]
		self.timing_screen = Sheet(self, headers=self.timing_headers, theme="dark blue", show_row_index=False)
		self.timing_screen.grid(row=5, column=0, pady=self.view.pady, columnspan=16, sticky="NSEW")

		# COMMENTARY LABEL
		self.commentary_label = customtkinter.CTkLabel(master=self, text="Lights Out And Away We Go!")
		self.commentary_label.grid(row=7, column=0, columnspan=16, pady=self.view.pady, sticky="NSEW")

	def update_view(self, data):
		self.lap_counter.configure(text=data["lap_counter"])
		self.timing_screen.set_sheet_data(data["standings"])
		
		for commentary in data["commentary"]:
			self.commentary_label.configure(text=commentary)
			

	def start_pause(self):
		self.view.controller.start_pause()

	def update_start_pause_btn(self, text):
		self.start_pause_btn.configure(text=text)

	def finish_race(self):
		self.start_pause_btn.configure(state="disabled")
