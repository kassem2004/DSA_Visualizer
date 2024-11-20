import tkinter as tk
import random
import threading
from algorithms.bubble_sort import bubble
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick
from algorithms.heap_sort import heap
from algorithms.insertion_sort import insertion
from algorithms.selection_sort import selection
from algorithms.suduko import isSafe, sudoku


class VisualizationFrame(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root, bg="#e6ffe6")
        self.app = app
        self.algorithm_name = None
        self.flag = False
        self.sort_array = ["Bubble Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Insertion Sort", "Selection Sort"]
        self.backtrack_array = ["N-Queens", "Sudoku Solver", "Knight's Tour"]
        self.search_array = ["Linear Search", "Binary Search"]
        self.current_board = None  # To store the current Sudoku board

        # Sidebar for controls
        self.sidebar = tk.Frame(self, bg="#ccffdd", width=200)
        self.sidebar.pack(side=tk.LEFT, fill="y")

        # Algorithm label (dynamic)
        self.algorithm_label = tk.Label(self.sidebar, text="", font=("Arial", 12, "bold"), bg="#ccffdd")
        self.algorithm_label.pack(pady=10)

        # Canvas for visualization
        self.visualization_canvas = tk.Canvas(self, bg="#e6ffe6")
        self.visualization_canvas.pack(fill="both", expand=True)

        # Data storage
        self.data = []

    def update_algorithm_label(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.algorithm_label.config(text=f"Algorithm: {algorithm_name}")
        self.create_sidebar_widgets(app=self.app)

    def create_sidebar_widgets(self, app):
        # Clear existing widgets
        for widget in self.sidebar.winfo_children():
            widget.destroy()

        self.algorithm_label = tk.Label(self.sidebar, text=f"Algorithm: {self.algorithm_name}", font=("Arial", 12, "bold"), bg="#ccffdd")
        self.algorithm_label.pack(pady=10)

        if self.algorithm_name in self.sort_array:
            tk.Label(self.sidebar, text="Size:", font=("Arial", 12), bg="#ccffdd").pack(pady=5)
            self.size_slider = tk.Scale(self.sidebar, from_=10, to=100, orient="horizontal", bg="#ccffdd")
            self.size_slider.pack(pady=5)

            tk.Label(self.sidebar, text="Speed:", font=("Arial", 12), bg="#ccffdd").pack(pady=5)
            self.speed_slider = tk.Scale(self.sidebar, from_=1, to=10, orient="horizontal", bg="#ccffdd")
            self.speed_slider.pack(pady=5)

            tk.Button(self.sidebar, text="Generate", command=self.generate_bars, font=("Arial", 10), height=1, width=10, bg="#66ff66").pack(pady=10)
            tk.Button(self.sidebar, text="Sort", command=self.start_sort, font=("Arial", 10), height=1, width=10, bg="#ff6666").pack(pady=10)
            tk.Button(self.sidebar, text="Back to Algorithms", font=("Arial", 10), height=1, width=15, command=app.show_algorithms_page, bg="#ff9999").pack(pady=10)
        elif self.algorithm_name == "Sudoku Solver":
            tk.Label(self.sidebar, text="Speed:", font=("Arial", 12), bg="#ccffdd").pack(pady=5)
            self.speed_slider = tk.Scale(self.sidebar, from_=1, to=10, orient="horizontal", bg="#ccffdd")
            self.speed_slider.pack(pady=5)

            tk.Button(self.sidebar, text="Generate", command=self.generate_grid, font=("Arial", 10), height=1, width=10, bg="#66ff66").pack(pady=10)
            tk.Button(self.sidebar, text="Solve", command=self.solve_sudoku, font=("Arial", 10), height=1, width=10, bg="#ff6666").pack(pady=10)
            tk.Button(self.sidebar, text="Back to Algorithms", font=("Arial", 10), height=1, width=15, command=app.show_algorithms_page, bg="#ff9999").pack(pady=10)

    def generate_bars(self):
        self.visualization_canvas.delete("all")
        size = self.size_slider.get()
        self.data = [random.randint(10, 300) for _ in range(size)]
        self.draw_bars()

    def generate_sudoku_board(self):
        """Efficient Sudoku board generation with predefined pattern and shuffling."""
        base_grid = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]

        def shuffle_rows_and_columns(grid):
            for i in range(0, 9, 3):
                random.shuffle(grid[i:i + 3])

            grid = list(map(list, zip(*grid)))

            for i in range(0, 9, 3):
                random.shuffle(grid[i:i + 3])
            return list(map(list, zip(*grid)))

        def shuffle_numbers(grid):
            mapping = list(range(1, 10))
            random.shuffle(mapping)
            number_map = {i + 1: mapping[i] for i in range(9)}

            for row in range(9):
                for col in range(9):
                    grid[row][col] = number_map[grid[row][col]]
            return grid

        def remove_numbers(board):
            """Remove numbers while ensuring the board has a unique solution."""
            cells_to_remove = 40  # Number of cells to remove
            attempts = 0
            while cells_to_remove > 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
                if board[row][col] != 0:
                    # Temporarily remove the number
                    temp = board[row][col]
                    board[row][col] = 0

                    # Check if the board still has a unique solution
                    if not has_unique_solution([row[:] for row in board]):
                        board[row][col] = temp  # Restore the number if no unique solution
                    else:
                        cells_to_remove -= 1

                attempts += 1
                # Avoid infinite loops (failsafe)
                if attempts > 200:
                    break
        def has_unique_solution(board):
            """Check if the Sudoku board has a unique solution."""
            solution_count = [0]
    
            def solve_and_count(board, row=0, col=0):
                if row == 9:
                    solution_count[0] += 1
                    return solution_count[0] <= 1  # Stop if more than one solution is found
    
                if col == 9:
                    return solve_and_count(board, row + 1, 0)
    
                if board[row][col] != 0:
                    return solve_and_count(board, row, col + 1)
    
                for num in range(1, 10):
                    if isSafe(board, row, col, num):
                        board[row][col] = num
                        if not solve_and_count(board, row, col + 1):
                            board[row][col] = 0
                            return False
                        board[row][col] = 0
    
                return True
    
            solve_and_count(board)
            return solution_count[0] == 1  # True if exactly one solution exists
                # Shuffle and create a puzzle
        shuffled_grid = shuffle_rows_and_columns(base_grid)
        randomized_grid = shuffle_numbers(shuffled_grid)
        puzzle_grid = remove_numbers(randomized_grid, difficulty=40)
        return puzzle_grid

    def draw_grid(self):
        """Draw the Sudoku grid."""
        if not self.current_board:
            return
    
        self.visualization_canvas.delete("all")
        canvas_width = self.visualization_canvas.winfo_width()
        canvas_height = self.visualization_canvas.winfo_height()
        cell_size = min(canvas_width, canvas_height) // 9  # Ensure square cells
    
        # Draw the grid lines
        for row in range(9):
            for col in range(9):
                x1, y1 = col * cell_size, row * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
    
                # Draw cell border
                self.visualization_canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
    
                # Fill numbers
                if self.current_board[row][col] != 0:
                    self.visualization_canvas.create_text(
                        x1 + cell_size // 2, y1 + cell_size // 2,  # Center of the cell
                        text=str(self.current_board[row][col]),
                        font=("Arial", int(cell_size * 0.5)),  # Dynamic font size
                        fill="black"
                    )
    
        # Draw thicker lines for 3x3 subgrids
        for i in range(0, 10, 3):
            self.visualization_canvas.create_line(0, i * cell_size, canvas_width, i * cell_size, width=4)
            self.visualization_canvas.create_line(i * cell_size, 0, i * cell_size, canvas_height, width=4)

    def generate_grid(self):
        def generate_and_draw():
            self.current_board = self.generate_sudoku_board()
            self.draw_grid()

        threading.Thread(target=generate_and_draw).start()

    def solve_sudoku(self):
        sudoku(self.current_board, 0, 0)
        self.draw_grid()

    def draw_bars(self, data=None, color="blue"):
        self.visualization_canvas.delete("all")
        data = data or self.data
        bar_width = self.visualization_canvas.winfo_width() / len(data)

        for i, value in enumerate(data):
            x0 = i * bar_width
            y0 = self.visualization_canvas.winfo_height() - value
            x1 = (i + 1) * bar_width
            y1 = self.visualization_canvas.winfo_height()
            self.visualization_canvas.create_rectangle(x0, y0, x1, y1, fill=color if isinstance(color, str) else color[i])
        self.update_idletasks()

    def start_sort(self):
        self.flag = True
        speed = 1 / self.speed_slider.get()

        if self.algorithm_name == "Bubble Sort":
            bubble(self.data, self.draw_bars, speed)
        elif self.algorithm_name == "Merge Sort":
            merge_sort(self.data, 0, len(self.data) - 1, self.draw_bars, speed)
        elif self.algorithm_name == "Quick Sort":
            quick(self.data, 0, len(self.data) - 1, self.draw_bars, speed)
        elif self.algorithm_name == "Heap Sort":
            heap(self.data, self.draw_bars, speed)
        elif self.algorithm_name == "Insertion Sort":
            insertion(self.data, self.draw_bars, speed)
        elif self.algorithm_name == "Selection Sort":
            selection(self.data, self.draw_bars, speed)
