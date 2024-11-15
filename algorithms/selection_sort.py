import time
def selection(arr, draw_bars, speed):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
                draw_bars(arr, ["green" if x < i else "red" if x == i else "yellow" if x == j else "blue" for x in range(len(arr))])
                time.sleep(speed)
        arr[i], arr[min] = arr[min], arr[i]
