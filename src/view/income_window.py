
import customtkinter

class IncomeWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def setup_widgets(self):
		self.sponsor_income_label = customtkinter.CTkLabel(self, text="Sponsor Income: 99", font=self.view.normal_font)
		self.sponsor_income_label.grid(row=1, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

	def configure_grid(self):
		pass

	def update_window(self, data):
		self.sponsor_income_label.configure(text=f"Sponsor Income: ${data['sponsor_income']:,}")
