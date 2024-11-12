import tkinter as tk

class DataStructuresFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#ffe6e6")
        self.app = app

        tk.Label(self, text="Data Structures", font=("Arial", 18), bg="#ffe6e6").pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=app.show_main_menu, bg="#ff9999")
        back_button.pack(pady=20)
