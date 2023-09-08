import customtkinter
from tksheet import Sheet


class StandingsWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(2, weight=1)
			

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="STANDINGS", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		customtkinter.CTkLabel(self, text="Drivers Championship", font=self.view.header1_font).grid(row=1,
										column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")
		
		self.driver_standings_sheet = Sheet(self, headers=["Name", "Points"], font=self.view.tksheet_normal_font, column_width=300, show_x_scrollbar=False,
				      					frame_bg="#333333", table_bg="#333333", table_fg="#ffffff", header_bg="#333333", header_fg="#ffffff",
										index_bg="#333333", index_fg="#ffffff", top_left_bg="#333333",
										header_font=self.view.tksheet_normal_font,
										index_font=self.view.tksheet_normal_font,
										)
		self.driver_standings_sheet.grid(row=2, column=0, padx=self.view.padx*5, pady=self.view.pady, sticky="NSEW")
		# self.driver_standings_sheet.change_theme(theme="dark blue", redraw=True)

		self.driver_standings_sheet.column_width(column=1, width=90)
		self.driver_standings_sheet.enable_bindings("single_select")
		self.driver_standings_sheet.bind("<ButtonPress-1>", self.click_driver_standing)

		customtkinter.CTkLabel(self, text="Teams Championship", font=self.view.header1_font).grid(row=1,
										column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")
		
		self.team_standings_sheet = self.view.setup_tksheet_table(self, ["Team", "Points"])
		self.team_standings_sheet.grid(row=2, column=1, padx=self.view.padx*5, pady=self.view.pady, sticky="NSEW")

		self.team_standings_sheet.column_width(column=1, width=90)
		self.team_standings_sheet.enable_bindings("single_select")
		self.team_standings_sheet.bind("<ButtonPress-1>", self.click_team_standing)

	def update_window(self, data):

		self.driver_standings_sheet.set_sheet_data(data=data["driver_standings"],
               reset_col_positions = False,
               reset_row_positions = True,
               redraw = True,
               verify = False,
               reset_highlights = False)

		self.team_standings_sheet.set_sheet_data(data=data["team_standings"],
               reset_col_positions = False,
               reset_row_positions = True,
               redraw = True,
               verify = False,
               reset_highlights = False)

	def click_driver_standing(self, event):
		currently_selected = self.driver_standings_sheet.get_currently_selected()
		if currently_selected:
			row = currently_selected.row
			column = currently_selected.column

			if column == 0:
				driver = self.driver_standings_sheet.get_cell_data(row, column)
				self.view.controller.show_driver_window(driver)
				self.driver_standings_sheet.deselect(row=row, column=column, redraw=True)

	def click_team_standing(self, event):
		currently_selected = self.team_standings_sheet.get_currently_selected()
		if currently_selected:
			row = currently_selected.row
			column = currently_selected.column

			if column == 0:
				team = self.team_standings_sheet.get_cell_data(row, column)
				self.view.controller.show_team_window(team)
				self.team_standings_sheet.deselect(row=row, column=column, redraw=True)		
