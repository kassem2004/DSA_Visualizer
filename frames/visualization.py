import tkinter as tk
import random
import time
from algorithms.bubble_sort import bubble
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick
from algorithms.heap_sort import heap
from algorithms.insertion_sort import insertion
from algorithms.selection_sort import selection

class VisualizationFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#e6ffe6")
        self.app = app
        self.algorithm_name = None
        self.flag = False

        sidebar = tk.Frame(self, bg="#ccffdd", width=200)
        sidebar.pack(side=tk.LEFT, fill="y")

        self.algorithm_label = tk.Label(sidebar, text="", font=("Arial", 12, "bold"), bg="#ccffdd")
        self.algorithm_label.pack(pady=10)

        tk.Label(sidebar, text="Size:", font=("Arial", 12), bg="#ccffdd").pack(pady=5)
        self.size_slider = tk.Scale(sidebar, from_=10, to=100, orient="horizontal", bg="#ccffdd")
        self.size_slider.pack(pady=5)

        tk.Label(sidebar, text="Speed:", font=("Arial", 12), bg="#ccffdd").pack(pady=5)
        self.speed_slider = tk.Scale(sidebar, from_=1, to=10, orient="horizontal", bg="#ccffdd")
        self.speed_slider.pack(pady=5)

        # Buttons
        tk.Button(sidebar, text="Shuffle", command=self.generate_bars, font=("Arial", 10), height=1, width=10, bg="#66ff66").pack(pady=10)
        tk.Button(sidebar, text="Sort", command=self.start_sort, font=("Arial", 10), height=1, width=10, bg="#ff6666").pack(pady=10)
        #tk.Button(sidebar, text="Stop", command=self.stop, font=("Arial", 10), height=1, width=10, bg="#ff6666").pack(pady=10)
        tk.Button(sidebar, text="Back to Algorithms", font=("Arial", 10), height=1, width=15, command=app.show_algorithms_page, bg="#ff9999").pack(pady=10)

        # Canvas for bar visualization
        self.visualization_canvas = tk.Canvas(self, bg="#e6ffe6")
        self.visualization_canvas.pack(fill="both", expand=True)

        self.data = []

    def update_algorithm_label(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.algorithm_label.config(text=f"Algorithm: {algorithm_name}")

    def generate_bars(self):
        self.visualization_canvas.delete("all")

        size = self.size_slider.get()
        self.data = [random.randint(10, 300) for _ in range(size)]

        self.draw_bars()

    def draw_bars(self, data=None, color="blue"):
        self.visualization_canvas.delete("all")
        data = data or self.data  # Use passed data if provided, else use self.data, this is for when used by algorithm
        bar_width = self.visualization_canvas.winfo_width() / len(data)
        
        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.visualization_canvas.winfo_height() - value
            x1 = (i + 1) * bar_width
            y1 = self.visualization_canvas.winfo_height()
            self.visualization_canvas.create_rectangle(x0, y0, x1, y1, fill=color if isinstance(color, str) else color[i])
        self.update_idletasks()

    def start_sort(self):
        # Calculate delay based on speed slider
        self.flag = True
        speed = 1 / self.speed_slider.get()
        if self.algorithm_name == "Bubble Sort":
            bubble(self.data, self.draw_bars, speed)
        elif self.algorithm_name == "Merge Sort":
            l = 0
            h = len(self.data) - 1
            merge_sort(self.data, l, h, self.draw_bars, speed)
        elif self.algorithm_name == "Quick Sort":
            l = 0
            h = len(self.data) - 1
            quick(self.data, l, h, self.draw_bars, speed)
        elif self.algorithm_name == "Heap Sort":
            heap(self.data, self.draw_bars, speed)
        elif self.algorithm_name == "Insertion Sort":
            insertion(self.data, self.draw_bars, speed)
        elif self.algorithm_name == "Selection Sort":
            selection(self.data, self.draw_bars, speed)
            self.draw_bars(self.data)
        else:
            self.flag = False
        if self.flag:
            self.draw_bars(color="green")

    #def stop(self):
    #    self.flag = False
