import customtkinter
from tksheet import Sheet


class CalenderWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)		

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="CALENDAR", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.calender_sheet = self.view.setup_tksheet_table(self, ["Week", "Race", "Circuit", "City", "Country"])
		self.calender_sheet.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		# self.calender_sheet.change_theme(theme="dark blue", redraw=True)
		self.calender_sheet.set_options(auto_resize_columns=True)

		self.calender_sheet.column_width(column=0, width=20)
		self.calender_sheet.column_width(column=1, width=240)
		self.calender_sheet.column_width(column=2, width=240)
		self.calender_sheet.column_width(column=3, width=70)
		self.calender_sheet.column_width(column=4, width=70)

		self.calender_sheet.enable_bindings("single_select")
		self.calender_sheet.bind("<ButtonPress-1>", self.click_calandar)


	def update_window(self, data):

		self.calender_sheet.set_sheet_data(data=data["calender"],
               reset_col_positions=False,
               reset_row_positions=True,
               redraw=True,
               verify=False,
               reset_highlights=False,
			   )

	def click_calandar(self, event):
		currently_selected = self.calender_sheet.get_currently_selected()
		if currently_selected:
			row = currently_selected.row
			column = currently_selected.column


			track = self.calender_sheet.get_cell_data(row, 2)
			self.view.controller.show_circuit_window(track)
			self.calender_sheet.deselect(row=row, column=column, redraw=True)