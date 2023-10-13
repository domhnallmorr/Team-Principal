import tkinter as tk

import customtkinter

def launch_window(controller, data):
	window = HireCommercialManagerWindow()
	window.data = data
	window.view = controller.view
	window.setup_widgets()

	window.focus()

	controller.app.wait_window(window)

	if window.button == "ok":
		return window.manager_selected
	else:
		return None

class HireCommercialManagerWindow(customtkinter.CTkToplevel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.geometry("700x300")
        
		self.title("Hire Commercial Manager")
		self.button = "cancel"
		self.grab_set()

	def configure_grid(self):
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(1, weight=1)

	def setup_widgets(self):

		scroll_frame = customtkinter.CTkScrollableFrame(self, width=200, height=200)
		scroll_frame.grid(row=1, column=1, sticky="NSEW")

		row = 1
		for idx, manager in enumerate(self.data["commercial_managers"]):
			label = customtkinter.CTkLabel(scroll_frame, text=manager.name, anchor="w")
			label.grid(row=row, column=1, padx=self.view.padx, pady=self.view.pady, sticky="EW")

			bar = customtkinter.CTkProgressBar(scroll_frame, orientation="horizontal")
			bar.grid(row=row, column=2, padx=self.view.padx, pady=self.view.pady, sticky="EW")
			bar.set(manager.reputation/100)

			button = customtkinter.CTkButton(scroll_frame, text="Hire", command=lambda idx=idx: self.hire(idx))
			button.grid(row=row, column=3, padx=self.view.padx, pady=self.view.pady, sticky="EW")
			row += 1

		cancel_button = customtkinter.CTkButton(self, text="Cancel", fg_color=self.view.warning_color,
					     							hover_color=self.view.warning_color_darker, command=self.cancel)
		cancel_button.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="E")

		self.configure_grid()


	def cancel(self):
		self.destroy()

	def hire(self, idx):
		self.button = "ok"

		self.manager_selected = self.data["commercial_managers"][idx]
		self.destroy()