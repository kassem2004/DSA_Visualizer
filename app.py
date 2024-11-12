import tkinter as tk
from frames.main_menu import MainMenuFrame
from frames.algorithms import AlgorithmsFrame
from frames.data_structures import DataStructuresFrame
from frames.visualization import VisualizationFrame

class DSAVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DSA Visualizer")
        self.root.geometry("800x400")

        # Initialize frames
        self.main_menu_frame = MainMenuFrame(self)
        self.algorithms_frame = AlgorithmsFrame(self)
        self.data_structures_frame = DataStructuresFrame(self)
        self.visualization_frame = VisualizationFrame(self)

        self.show_main_menu()

    def run(self):
        self.root.mainloop()

    def show_main_menu(self):
        self._forget_all_frames()
        self.main_menu_frame.pack(fill="both", expand=True)

    def show_algorithms_page(self):
        self._forget_all_frames()
        self.algorithms_frame.pack(fill="both", expand=True)

    def show_data_structures_page(self):
        self._forget_all_frames()
        self.data_structures_frame.pack(fill="both", expand=True)

    def show_visualization_page(self, algorithm_name):
        self._forget_all_frames()
        self.visualization_frame.update_algorithm_label(algorithm_name)
        self.visualization_frame.pack(fill="both", expand=True)

    def _forget_all_frames(self):
        for frame in [self.main_menu_frame, self.algorithms_frame, self.data_structures_frame, self.visualization_frame]:
            frame.pack_forget()
