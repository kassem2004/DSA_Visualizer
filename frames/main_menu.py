import tkinter as tk

class MainMenuFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#f0f0f5")
        self.app = app

        tk.Label(self, text="Choose which to visualize:", font=("Arial", 18), bg="#f0f0f5").pack(pady=20)

        button_frame = tk.Frame(self, bg="#f0f0f5")
        button_frame.pack(pady=50)

        algorithms_button = tk.Button(button_frame, text="Algorithms", font=("Arial", 14), width=15,
                                      command=app.show_algorithms_page, bg="LIGHTBLUE")
        algorithms_button.pack(side=tk.LEFT, padx=10)

        data_structures_button = tk.Button(button_frame, text="Data Structures", font=("Arial", 14), width=15,
                                           command=app.show_data_structures_page, bg="RED")
        data_structures_button.pack(side=tk.LEFT, padx=10)
