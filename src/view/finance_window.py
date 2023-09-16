import customtkinter

from view import treeview_functions

class FinanceWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def configure_grid(self):
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)

		self.summary_tab.grid_columnconfigure(0, weight=1)
		self.summary_tab.grid_rowconfigure(0, weight=1)

	def setup_widgets(self):
		customtkinter.CTkLabel(self, text="FINANCES", font=self.view.page_title_font).grid(row=0,
										     column=0, padx=self.view.padx*3, pady=self.view.pady, sticky="NW")
		
		self.tabview = customtkinter.CTkTabview(self)
		self.tabview.grid(row=1, column=0, sticky="NSEW")
		
		self.tabview.add("Summary")
		self.summary_tab = self.tabview.tab("Summary")

		self.tabview.add("Income")
		self.income_tab = self.tabview.tab("Income")

		self.tabview.add("Expenditure")
		self.expenditure_tab = self.tabview.tab("Expenditure")