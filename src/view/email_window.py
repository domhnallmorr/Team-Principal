import copy
import customtkinter

class EmailWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=4)
		self.grid_rowconfigure(1, weight=1)	

		self.email_list_frame.grid_columnconfigure(1, weight=1)	

		self.email_content_frame.grid_rowconfigure(1, weight=1)		
		self.email_content_frame.grid_columnconfigure(1, weight=1)		

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="EMAIL", font=self.view.page_title_font).grid(row=0,
										     column=0, columnspan=2, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.email_list_frame = customtkinter.CTkScrollableFrame(self)
		self.email_list_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.email_content_frame = customtkinter.CTkFrame(self)
		self.email_content_frame.grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.message_textbox = customtkinter.CTkTextbox(self.email_content_frame, font=self.view.normal_font, wrap="word")
		self.message_textbox.grid(row=1, column=1, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.message_textbox.configure(state="disabled")

	def update_window(self, data):

		self.buttons = []
		self.emails = copy.deepcopy(data["emails"])

		for idx, mail in enumerate(self.emails):
			subject = mail[0]
			btn = customtkinter.CTkButton(self.email_list_frame, text=subject, height=60, width=200, corner_radius=0,
								 anchor="w", command=lambda email_idx=idx: self.show_email(email_idx))
			btn.grid(row=idx, column=1, sticky="NSEW")

	def show_email(self, idx):
		msg = self.emails[idx][1]

		self.message_textbox.configure(state="normal")
		self.message_textbox.delete("0.0", "end")
		self.message_textbox.insert("0.0", msg)
		self.message_textbox.configure(state="disabled")