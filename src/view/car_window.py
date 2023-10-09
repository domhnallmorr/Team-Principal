import customtkinter

class CarWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		pass

	def setup_widgets(self):
		self.title_label = customtkinter.CTkLabel(self, text="Car", font=self.view.page_title_font)
		self.title_label.grid(row=0, column=0, columnspan=2, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		self.speed_label = customtkinter.CTkLabel(self, text="Speed:", font=self.view.normal_font)
		self.speed_label.grid(row=2, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

	def update_window(self, data):
		self.speed_label.configure(text=f'Speed: {data["speed"]}')
