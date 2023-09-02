import customtkinter
from tksheet import Sheet


class CalenderWindow(customtkinter.CTkFrame):
	def __init__(self, master, view, default_year):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.year_combo.set(default_year)
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(3, weight=1)		

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="CALENDAR", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		self.year_combo = customtkinter.CTkComboBox(self, command=self.combobox_callback)
		self.year_combo.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.calender_sheet = self.view.setup_tksheet_table(self, ["Week", "Race", "Circuit", "City", "Country", "Winner"])
		self.calender_sheet.grid(row=3, column=0, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
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
		
		self.year_combo.set(data["year"])
		self.calender_sheet.set_sheet_data(data=data["calender"],
               reset_col_positions=False,
               reset_row_positions=True,
               redraw=True,
               verify=False,
               reset_highlights=False,
			   )

		self.year_combo.configure(values=data["years"])

	def click_calandar(self, event):
		currently_selected = self.calender_sheet.get_currently_selected()
		if currently_selected:
			row = currently_selected.row
			column = currently_selected.column

			if column != 5:
				track = self.calender_sheet.get_cell_data(row, 2)
				self.view.controller.show_circuit_window(track)
				self.calender_sheet.deselect(row=row, column=column, redraw=True)
			else:
				self.view.controller.show_race_result(int(self.year_combo.get()), row)

	def combobox_callback(self, event):
		self.view.controller.update_calender_window(int(self.year_combo.get()))