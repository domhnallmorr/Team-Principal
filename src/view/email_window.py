import copy
from tkinter import ttk
import tkinter as tk

import customtkinter

from view import treeview_functions

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
		self.email_list_frame.grid_rowconfigure(1, weight=1)

		self.email_content_frame.grid_rowconfigure(1, weight=1)		
		self.email_content_frame.grid_columnconfigure(1, weight=1)	

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="EMAIL", font=self.view.page_title_font).grid(row=0,
										     column=0, columnspan=2, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.email_list_frame = customtkinter.CTkFrame(self)
		self.email_list_frame.grid(row=1, column=0, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.email_content_frame = customtkinter.CTkFrame(self)
		self.email_content_frame.grid(row=1, column=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")

		self.email_list = ttk.Treeview(self.email_list_frame, selectmode="extended", show="tree")# columns=columns, show="tree")
		self.email_list.grid(row=1, column=1, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.email_list.column("#0", stretch=tk.YES)
		self.email_list.bind('<<TreeviewSelect>>',lambda event, : self.single_click(event))
		self.email_list.tag_configure('bold', font=("Verdana", 12, "bold"))

		ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.email_list_frame, command=self.email_list.yview)
		ctk_textbox_scrollbar.grid(row=1, column=2, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.email_list.configure(yscrollcommand=ctk_textbox_scrollbar.set)


		self.message_textbox = customtkinter.CTkTextbox(self.email_content_frame, font=self.view.normal_font, wrap="word")
		self.message_textbox.grid(row=1, column=1, columnspan=1, padx=self.view.padx, pady=self.view.pady, sticky="NSEW")
		self.message_textbox.configure(state="disabled")

	def update_window(self, data):

		self.buttons = []
		self.emails = copy.deepcopy(data["emails"])

		data = [[m[0]] for m in self.emails]
		treeview_functions.write_data_to_treeview_general(self.email_list, "replace", data)


	def show_email(self, idx):
		msg = self.emails[idx][1]

		self.message_textbox.configure(state="normal")
		self.message_textbox.delete("0.0", "end")
		self.message_textbox.insert("0.0", msg)
		self.message_textbox.configure(state="disabled")

	def single_click(self, event):

		selected_item = self.email_list.selection()
		if selected_item:  # Check if any item is selected
			idx = self.email_list.index(selected_item[0])
			self.show_email(idx)