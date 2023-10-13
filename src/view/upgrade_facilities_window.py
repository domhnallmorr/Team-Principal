import tkinter as tk

import customtkinter

def launch_window(controller, data):
	window = UpgradeFacilitiesWindow()
	window.data = data
	window.view = controller.view
	window.setup_widgets()

	window.focus()

	controller.app.wait_window(window)

	if window.button == "ok":
		data = {
			"facility": window.facility,
			"upgrade_type": window.upgrade_type,
		}
		return data
	else:
		return None

class UpgradeFacilitiesWindow(customtkinter.CTkToplevel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.geometry("330x160") # wxh
        
		self.title("Upgrade Facilities")
		self.button = "cancel"
		self.grab_set()

	def configure_grid(self):
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)

	def setup_widgets(self):

		label = customtkinter.CTkLabel(self, text="Select Facility:", anchor="e")
		label.grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="EW")

		self.facility_combo = customtkinter.CTkComboBox(self, values=["Wind Tunnel", "Super Computer", "Engine Factory", "Chassis Workshop", "Brake Center"],
                                     command=self.combobox_callback, state="readonly")
		self.facility_combo.grid(row=1, column=2, padx=self.view.padx, pady=self.view.pady, sticky="EW")
		
		label = customtkinter.CTkLabel(self, text="Select Upgrade Type:", anchor="e")
		label.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="EW")

		self.upgrade_combo = customtkinter.CTkComboBox(self, values=["Minor", "Major"],
                                     command=self.combobox_callback, state="readonly")
		self.upgrade_combo.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="EW")

		self.cost_label = customtkinter.CTkLabel(self, text="Estimated Cost:")
		self.cost_label.grid(row=3, column=1, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="EW")

		self.upgrade_btn = customtkinter.CTkButton(self, text="Upgrade", state="disabled", command=self.upgrade)
		self.upgrade_btn.grid(row=4, column=1, padx=self.view.padx, pady=self.view.pady, sticky="EW")
		
		self.cancel_btn = customtkinter.CTkButton(self, text="Cancel", fg_color=self.view.warning_color,
					     							hover_color=self.view.warning_color_darker, command=self.cancel)
		self.cancel_btn.grid(row=4, column=2, padx=self.view.padx, pady=self.view.pady, sticky="EW")

		self.configure_grid()

	def combobox_callback(self, event=None):
		if self.facility_combo.get() == "" or self.upgrade_combo.get() == "":
			pass
		else:
			self.upgrade_btn.configure(state="normal")
			if self.upgrade_combo == "Minor":
				estimated_cost = 3_000_000
			else:
				estimated_cost = 15_000_000

			self.cost_label.configure(text=f"Estimated Cost: {estimated_cost:,}")

	def cancel(self):
		self.destroy()

	def upgrade(self):
		self.button = "ok"

		self.facility = self.facility_combo.get()
		self.upgrade_type = self.upgrade_combo.get()

		self.destroy()