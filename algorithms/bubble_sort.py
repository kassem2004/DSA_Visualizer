import time

def bubble(arr, draw_bars, speed, frame):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(arr, ["red" if x == j or x == j + 1 else "blue" for x in range(n)])
                time.sleep(speed)  # Control the speed of visualization with a delay
