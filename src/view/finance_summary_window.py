import copy
from tkinter import ttk
import tkinter as tk

import customtkinter

import matplotlib
from matplotlib.ticker import FuncFormatter
from matplotlib import style
style.use('dark_background')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from view import treeview_functions

class FinanceSummaryWindow(customtkinter.CTkFrame):
	def __init__(self, master, view):
		super().__init__(master)

		self.view = view

		self.setup_widgets()
		self.configure_grid()

	def setup_widgets(self):
		# BALANCE
		customtkinter.CTkLabel(self, text="OVERALL BALANCE", font=self.view.header2_font).grid(row=1,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")

		self.balance_figure = Figure(figsize=(5,5), dpi=100)
		self.balance_axis = self.balance_figure.add_subplot(111)

		self.balance_canvas = FigureCanvasTkAgg(self.balance_figure, self)
		self.balance_canvas.draw()
		self.balance_canvas.get_tk_widget().grid(row=2, column=0, columnspan=8, pady=2,sticky="nsew")	

		# PROFIT/LOSS
		customtkinter.CTkLabel(self, text="PROFIT/LOSS", font=self.view.header2_font).grid(row=3,
										     column=0, padx=self.view.padx, pady=self.view.pady, sticky="NW")		

		self.profit_this_month_label = customtkinter.CTkLabel(self, text="This Month:", font=self.view.normal_font)
		self.profit_this_month_label.grid(row=4, column=0, padx=self.view.padx, pady=self.view.pady, sticky="nsew")	

		self.profit_this_season_label = customtkinter.CTkLabel(self, text="This Season:", font=self.view.normal_font)
		self.profit_this_season_label.grid(row=4, column=6, padx=self.view.padx, pady=self.view.pady, sticky="e")	

		self.profit_last_season_label = customtkinter.CTkLabel(self, text="Last Season:", font=self.view.normal_font)
		self.profit_last_season_label.grid(row=4, column=7, padx=self.view.padx, pady=self.view.pady)	

		self.profit_figure = Figure(figsize=(5,5), dpi=100)
		self.profit_axis = self.profit_figure.add_subplot(111)

		self.profit_canvas = FigureCanvasTkAgg(self.profit_figure, self)
		self.profit_canvas.draw()
		self.profit_canvas.get_tk_widget().grid(row=5, column=0, columnspan=8, padx=self.view.padx, pady=self.view.pady, sticky="nsew")	

	def configure_grid(self):
		self.grid_columnconfigure(6, weight=1)
		self.grid_columnconfigure(7, weight=1)
		self.grid_rowconfigure(2, weight=1)
		self.grid_rowconfigure(5, weight=1)

	def update_window(self, data):
		y_formatter = FuncFormatter(self.balance_formatter)

		# BALANCE
		df = data["historical_balance"]
		self.balance_axis.cla()
		x = df['Timestamp']
		y = df['Balance']
		self.balance_axis.plot(x, y)
		self.balance_axis.fill_between(x, y, 0, color='lightblue', alpha=0.5)

		self.balance_figure.gca().yaxis.set_major_formatter(y_formatter)
		self.balance_axis.grid()
		self.balance_figure.tight_layout()
		self.balance_canvas.draw()

		# Profit/Loss
		df = data["historical_profit"]
		self.profit_axis.cla()
		
		if df.empty is False: # data not available until 4 weeks have passed (i.e. 1 month)
			x = df["Timestamp"]
			y = df["Profit_Loss"]
			self.profit_axis.plot(x, y)
			self.profit_axis.fill_between(x, y, 0, color="lightblue", alpha=0.5)

			self.profit_figure.gca().yaxis.set_major_formatter(y_formatter)
		self.profit_axis.grid()
		self.profit_figure.tight_layout()
		self.profit_canvas.draw()

		# Update Labels
		self.profit_this_month_label.configure(text=f"This Month: ${data['profit_this_month']:,}")
		self.profit_this_season_label.configure(text=f"This Season: ${data['profit_this_season']:,}")
		if data["profit_last_season"] == "-":
			self.profit_last_season_label.configure(text=f"Last Season: ${data['profit_last_season']}")
		else:
			self.profit_last_season_label.configure(text=f"Last Season: ${data['profit_last_season']:,}")

	def balance_formatter(self, x, pos):
		if x < 1_000_000:
			return f"${int(x/1_000)}K"
		else:
			return f"${int(x/1_000_000)}M"
			
