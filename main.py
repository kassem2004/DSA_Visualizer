import tkinter as tk
from tkinter import ttk

class DSAVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DSA Visualizer")
        self.root.geometry("800x400")
        
        # Main frames for each "page"
        self.main_menu_frame = tk.Frame(self.root, bg="#f0f0f5")
        self.algorithms_frame = tk.Frame(self.root, bg="#e6f2ff")
        self.data_structures_frame = tk.Frame(self.root, bg="#ffe6e6")
        self.visualization_frame = tk.Frame(self.root, bg="#e6ffe6")

        self.setup_main_menu()
        self.setup_algorithms_page()
        self.setup_data_structures_page()
        self.setup_visualization_page()

        self.main_menu_frame.pack(fill="both", expand=True)

        self.root.mainloop()

    def setup_main_menu(self):
        header = tk.Label(self.main_menu_frame, text="Choose which to visualize:", font=("Arial", 18), bg="#f0f0f5")
        header.pack(pady=20)

        button_frame = tk.Frame(self.main_menu_frame, bg="#f0f0f5")
        button_frame.pack(pady=50)

        algorithms_button = tk.Button(button_frame, text="Algorithms", font=("Arial", 14), width=15,
                                      command=self.show_algorithms_page, bg="LIGHTBLUE")
        algorithms_button.pack(side=tk.LEFT, padx=10)

        data_structures_button = tk.Button(button_frame, text="Data Structures", font=("Arial", 14), width=15,
                                           command=self.show_data_structures_page, bg="RED")
        data_structures_button.pack(side=tk.LEFT, padx=10)

    def setup_algorithms_page(self):
        tk.Label(self.algorithms_frame, text="Algorithms", font=("Arial", 18), bg="BLUE").pack(pady=20)

        type_label = tk.Label(self.algorithms_frame, text="Choose Type:", font=("Arial", 14))
        type_label.pack()

        self.algorithm_type = tk.StringVar()
        type_dropdown = ttk.Combobox(self.algorithms_frame, textvariable=self.algorithm_type, state="readonly",
                                     values=["Search", "Sort", "Backtracking"])
        type_dropdown.pack(pady=5)
        type_dropdown.bind("<<ComboboxSelected>>", self.update_algorithm_options)

        specific_label = tk.Label(self.algorithms_frame, text="Choose Algorithm:", font=("Arial", 14))
        specific_label.pack()

        self.algorithm_option = tk.StringVar()
        self.specific_dropdown = ttk.Combobox(self.algorithms_frame, textvariable=self.algorithm_option, state="readonly")
        self.specific_dropdown.pack(pady=5)

        visualize_button = tk.Button(self.algorithms_frame, text="Visualize", command=self.show_visualization_page,
                                     bg="PURPLE", font=("Arial", 14), width=10)
        visualize_button.pack(pady=20)

        back_button = tk.Button(self.algorithms_frame, text="Back to Main Menu", command=self.show_main_menu, bg="#ff9999")
        back_button.pack(pady=10)

    def setup_data_structures_page(self):
        tk.Label(self.data_structures_frame, text="Data Structures", font=("Arial", 18)).pack(pady=20)

        back_button = tk.Button(self.data_structures_frame, text="Back to Main Menu", command=self.show_main_menu, bg="#ff9999")
        back_button.pack(pady=20)

    def setup_visualization_page(self):
        # Sidebar for algorithm info and controls
        sidebar = tk.Frame(self.visualization_frame, bg="#ccffdd", width=200)
        sidebar.pack(side=tk.LEFT, fill="y")

        self.selected_algorithm_label = tk.Label(sidebar, text="Algorithm: (None Selected)", font=("Arial", 12, "bold"),
                                                 bg="#ccffdd")
        self.selected_algorithm_label.pack(pady=10)

        size_label = tk.Label(sidebar, text="Size:", font=("Arial", 12), bg="#ccffdd")
        size_label.pack(pady=5)
        self.size_slider = tk.Scale(sidebar, from_=10, to=100, orient="horizontal", bg="#ccffdd")
        self.size_slider.pack(pady=5)

        speed_label = tk.Label(sidebar, text="Speed:", font=("Arial", 12), bg="#ccffdd")
        speed_label.pack(pady=5)
        self.speed_slider = tk.Scale(sidebar, from_=1, to=10, orient="horizontal", bg="#ccffdd")
        self.speed_slider.pack(pady=5)

        shuffle_button = tk.Button(sidebar, text="Shuffle", font=("Arial", 12), width=10, bg="#66ff66")
        shuffle_button.pack(pady=10)

        sort_button = tk.Button(sidebar, text="Sort", font=("Arial", 12), width=10, bg="#ff6666")
        sort_button.pack(pady=10)

        back_button = tk.Button(sidebar, text="Back to Algorithms", font=("Arial", 12), width=15, command=self.show_algorithms_page, bg="#ff9999")
        back_button.pack(pady=10)

        # Visualization canvas area
        self.visualization_canvas = tk.Canvas(self.visualization_frame, bg="#e6ffe6")
        self.visualization_canvas.pack(fill="both", expand=True)

    def update_algorithm_options(self, event):
        selected_type = self.algorithm_type.get()
        if selected_type == "Search":
            options = ["Linear Search", "Binary Search"]
        elif selected_type == "Sort":
            options = ["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort", "Selection Sort"]
        elif selected_type == "Backtracking":
            options = ["N-Queens", "Sudoku Solver", "Knight's Tour"]
        else:
            options = []

        self.specific_dropdown['values'] = options
        self.specific_dropdown.set("")

    def show_main_menu(self):
        self.algorithms_frame.pack_forget()
        self.data_structures_frame.pack_forget()
        self.visualization_frame.pack_forget()
        self.main_menu_frame.pack(fill="both", expand=True)

    def show_algorithms_page(self):
        self.main_menu_frame.pack_forget()
        self.data_structures_frame.pack_forget()
        self.visualization_frame.pack_forget()
        self.algorithms_frame.pack(fill="both", expand=True)

    def show_data_structures_page(self):
        self.main_menu_frame.pack_forget()
        self.algorithms_frame.pack_forget()
        self.visualization_frame.pack_forget()
        self.data_structures_frame.pack(fill="both", expand=True)

    def show_visualization_page(self):
        selected_algorithm = self.algorithm_option.get()
        self.selected_algorithm_label.config(text=f"Algorithm: {selected_algorithm if selected_algorithm else '(None Selected)'}")
        
        self.main_menu_frame.pack_forget()
        self.algorithms_frame.pack_forget()
        self.data_structures_frame.pack_forget()
        self.visualization_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    DSAVisualizer()
