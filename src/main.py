import customtkinter

from tp_controller import tp_controller

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("Team Principal V0.0.8")
controller = tp_controller.TPController(app)

app.after(0, lambda:app.state('zoomed'))
app.mainloop()
app.mainloop()
