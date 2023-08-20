import customtkinter
from tksheet import Sheet


class CircuitWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure(1, weight=1)
			
		self.main_frame.grid_columnconfigure(2, weight=1)
		self.main_frame.grid_rowconfigure(2, weight=1)
		self.main_frame.grid_rowconfigure(3, weight=1)

	def setup_widgets(self):
		self.title_label = customtkinter.CTkLabel(self, text="Circuit", font=self.view.page_title_font)
		self.title_label.grid(row=0, column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")

		self.main_frame = customtkinter.CTkFrame(self)
		self.main_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.attributes_frame = customtkinter.CTkFrame(self)
		self.attributes_frame.grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.track_map_image_label =  customtkinter.CTkLabel(self.main_frame, text="")
		self.track_map_image_label.grid(row=1, column=1, rowspan=1, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.city_label = customtkinter.CTkLabel(self.main_frame, text="City:", font=self.view.normal_font)
		self.city_label.grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.country_label = customtkinter.CTkLabel(self.main_frame, text="Country:", font=self.view.normal_font)
		self.country_label.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.length_label = customtkinter.CTkLabel(self.main_frame, text="Length (km):", font=self.view.normal_font)
		self.length_label.grid(row=3, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.laps_label = customtkinter.CTkLabel(self.main_frame, text="Laps:", font=self.view.normal_font)
		self.laps_label.grid(row=3, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.description_textbox = customtkinter.CTkTextbox(self.main_frame, font=self.view.normal_font, wrap="word")
		self.description_textbox.grid(row=5, column=1, columnspan=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		# ATTRIBUTES
		customtkinter.CTkLabel(self.attributes_frame, text="Downforce:", font=self.view.normal_font).grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.downforce_progressbar = customtkinter.CTkProgressBar(self.attributes_frame, orientation="horizontal")
		self.downforce_progressbar.grid(row=1, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.attributes_frame, text="Grip:", font=self.view.normal_font).grid(row=2, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.grip_progressbar = customtkinter.CTkProgressBar(self.attributes_frame, orientation="horizontal")
		self.grip_progressbar.grid(row=2, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.attributes_frame, text="Top Speed:", font=self.view.normal_font).grid(row=3, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.top_speed_progressbar = customtkinter.CTkProgressBar(self.attributes_frame, orientation="horizontal")
		self.top_speed_progressbar.grid(row=3, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		customtkinter.CTkLabel(self.attributes_frame, text="Braking:", font=self.view.normal_font).grid(row=4, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.braking_progressbar = customtkinter.CTkProgressBar(self.attributes_frame, orientation="horizontal")
		self.braking_progressbar.grid(row=4, column=2, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

	def update_window(self, data):
		self.title_label.configure(text=f'Circuit: {data["name"]}')

		self.track_image = customtkinter.CTkImage(light_image=self.view.track_maps[data["name"]], size=(768, 383))
		self.track_map_image_label.configure(image=self.track_image)

		self.city_label.configure(text=f'City: {data["city"]}')
		self.country_label.configure(text=f'Country: {data["country"]}')
		self.length_label.configure(text=f'Length (km): {data["length"]}')
		self.laps_label.configure(text=f'Laps: {data["laps"]}')

		self.description_textbox.configure(state="normal")
		self.description_textbox.delete("0.0", "end")
		self.description_textbox.insert("0.0", data["description"])
		self.description_textbox.configure(state="disabled")

		self.downforce_progressbar.set(data["downforce"]/100)
		self.grip_progressbar.set(data["grip"]/100)
		self.top_speed_progressbar.set(data["top_speed"]/100)
		self.braking_progressbar.set(data["braking"]/100)
