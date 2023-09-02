import customtkinter
from tksheet import Sheet


class ResultsWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(2, weight=1)		

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="RESULTS", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		self.race_title_label = customtkinter.CTkLabel(self, text="Race of X XXXX", font=self.view.header1_font)
		self.race_title_label.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.results_sheet = self.view.setup_tksheet_table(self, headers=["Name", "Team", "Time"])
		self.results_sheet.grid(row=2, column=0, padx=50, pady=self.view.pady, sticky="NSEW")


		# self.advance_btn = customtkinter.CTkButton(self, text="Advance", command=self.view.controller.go_to_race)
		# self.advance_btn.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

	def update_window(self, data):

		self.results_sheet.set_sheet_data(data=data["results"],
               reset_col_positions = True,
               reset_row_positions = True,
               redraw = True,
               verify = False,
               reset_highlights = False)
		
		self.race_title_label.configure(text=data["race_title"])
