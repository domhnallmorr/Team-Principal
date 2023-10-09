
import customtkinter

class SponsorsWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def setup_widgets(self):
		self.title_label = customtkinter.CTkLabel(self, text="Sponsors", font=self.view.page_title_font)
		self.title_label.grid(row=0, column=0, columnspan=2, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		self.commercial_manager_label = customtkinter.CTkLabel(self, text="Commercial Manager: Someone", font=self.view.normal_font)
		self.commercial_manager_label.grid(row=1, column=0, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.race_label = customtkinter.CTkLabel(self, text="Reputation:", font=self.view.normal_font)
		self.race_label.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.reputation_progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal")
		self.reputation_progressbar.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.hire_btn = customtkinter.CTkButton(master=self, text="Hire Commercial Manager", command=self.view.controller.hire_commercial_manager)
		self.hire_btn.grid(row=3, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

	def configure_grid(self):
		pass

	def update_window(self, data):
		self.commercial_manager_label.configure(text=f"Commercial Manager: {data['commercial_manager']}")
		self.reputation_progressbar.set(data["reputation"]/100)
