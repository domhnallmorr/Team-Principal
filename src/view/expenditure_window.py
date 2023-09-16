
import customtkinter

class ExpenditureWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def setup_widgets(self):
		self.wages_label = customtkinter.CTkLabel(self, text="Wages: 99", font=self.view.normal_font)
		self.wages_label.grid(row=1, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.race_label = customtkinter.CTkLabel(self, text="Cost per Race: 99", font=self.view.normal_font)
		self.race_label.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

	def configure_grid(self):
		pass

	def update_window(self, data):
		self.wages_label.configure(text=f"Sponsor Income: ${data['wages']:,}")
		self.race_label.configure(text=f"Cost per Race: ${data['cost_per_race']:,}")
