import tkinter as tk
from tkinter import ttk

class AlgorithmsFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#e6f2ff")
        self.app = app

        tk.Label(self, text="Algorithms", font=("Arial", 18), bg="BLUE").pack(pady=20)

        type_label = tk.Label(self, text="Choose Type:", font=("Arial", 14))
        type_label.pack()

        self.algorithm_type = tk.StringVar()
        type_dropdown = ttk.Combobox(self, textvariable=self.algorithm_type, state="readonly",
                                     values=["Search", "Sort", "Backtracking"])
        type_dropdown.pack(pady=5)
        type_dropdown.bind("<<ComboboxSelected>>", self.update_algorithm_options)

        specific_label = tk.Label(self, text="Choose Algorithm:", font=("Arial", 14))
        specific_label.pack()

        self.algorithm_option = tk.StringVar()
        self.specific_dropdown = ttk.Combobox(self, textvariable=self.algorithm_option, state="readonly")
        self.specific_dropdown.pack(pady=5)

        visualize_button = tk.Button(self, text="Visualize", command=self.on_visualize,
                                     bg="PURPLE", font=("Arial", 14), width=10)
        visualize_button.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=app.show_main_menu, bg="#ff9999")
        back_button.pack(pady=10)

    def update_algorithm_options(self, event):
        selected_type = self.algorithm_type.get()
        options = []
        if selected_type == "Search":
            options = ["Linear Search", "Binary Search"]
        elif selected_type == "Sort":
            options = ["Bubble Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Insertion Sort", "Selection Sort"]
        elif selected_type == "Backtracking":
            options = ["N-Queens", "Sudoku Solver", "Knight's Tour"]
        self.specific_dropdown['values'] = options
        self.specific_dropdown.set("")

    def on_visualize(self):
        algorithm_name = self.algorithm_option.get()
        self.app.show_visualization_page(algorithm_name)
