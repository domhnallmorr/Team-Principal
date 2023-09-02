import customtkinter
from tksheet import Sheet


class MainWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(1, weight=1)

		self.header_frame.grid_columnconfigure(8, weight=1)
		self.sidebar_frame.grid_rowconfigure(20, weight=1)

		self.page_frame.grid_columnconfigure(0, weight=1)
		self.page_frame.grid_rowconfigure(0, weight=1)

	def setup_widgets(self):
		self.header_frame = customtkinter.CTkFrame(self)
		self.header_frame.grid(row=0, column=0, columnspan=2, sticky="EW")
	
		self.sidebar_frame = customtkinter.CTkFrame(self)
		self.sidebar_frame.grid(row=1, column=0, padx=self.view.padx, sticky="NSEW")

		self.page_frame = customtkinter.CTkFrame(self)
		self.page_frame.grid(row=1, column=1, padx=self.view.padx, sticky="NSEW")

		# HEADER LABELS
		self.header_label = customtkinter.CTkLabel(self.header_frame, text="Moretti $1,000,000", font=self.view.normal_font)
		self.header_label.grid(row=0, column=0, padx=self.view.padx, sticky="NW")

		self.week_label = customtkinter.CTkLabel(self.header_frame, text="Week 1 1998", font=self.view.normal_font)
		self.week_label.grid(row=0, column=8, padx=self.view.padx, sticky="NE")

		# SIDEBAR BUTTONS
		self.email_btn = customtkinter.CTkButton(master=self.sidebar_frame, text="Email",
										   command=lambda window="email": self.view.change_window(window))
		self.email_btn.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.team_btn = customtkinter.CTkButton(master=self.sidebar_frame, text="Team")# command=self.start_pause)
		self.team_btn.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.standings_btn = customtkinter.CTkButton(master=self.sidebar_frame, text="Standings",
					       command=lambda window="standings": self.view.change_window(window))
		self.standings_btn.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.calender_btn = customtkinter.CTkButton(master=self.sidebar_frame, text="Calendar",
					      command=lambda window="calender": self.view.change_window(window))
		self.calender_btn.grid(row=4, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")


		self.advance_btn = customtkinter.CTkButton(master=self.sidebar_frame, text="Advance", fg_color=self.view.success_color,
					     							hover_color=self.view.success_color_darker, command=self.view.controller.advance)
		self.advance_btn.grid(row=20, column=0, padx=self.view.padx, pady=self.view.pady, sticky="SW")

	def update_window(self, data):
		self.week_label.configure(text=data["date"])

		if data["in_race_week"] is True:
			self.advance_btn.configure(text="Go To Race Weekend", command=lambda window="race_weekend": self.view.change_window(window))
		else:
			self.advance_btn.configure(text="Advance")
		

	def update_advance_btn(self, mode):
		if mode == "advance":
			self.advance_btn.configure(text="Advance", command=self.view.controller.advance)
		else:
			self.advance_btn.configure(text="Go To Race Weekend", command=lambda window="race_weekend": self.view.change_window(window))
