import time
def heapify(arr, n, idx, draw_bars, speed):
    largest = idx
    # Child nodes of largest
    l = 2*idx + 1
    r = 2*idx + 2

    draw_bars(arr, ["red" if x == idx else "yellow" if x == l or x == r else "blue" for x in range(len(arr))])
    time.sleep(speed)

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        draw_bars(arr, ["red" if x == largest or x == idx else "yellow" if x == l or x == r else "blue" for x in range(len(arr))])
        time.sleep(speed)
        heapify(arr, n, largest, draw_bars, speed) # Recursively fix affected subtree

def heap(arr, draw_bars, speed):
    n = len(arr)

    start = (n // 2) - 1 # First non-leaf node

    for i in range(start, -1, -1):
        heapify(arr, n, i, draw_bars, speed)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        draw_bars(arr, ["green" if x >= i else "red" if x == 0 else "blue" for x in range(len(arr))])
        time.sleep(speed)
        heapify(arr, i, 0, draw_bars, speed)
    draw_bars(arr, ["green" for _ in range(len(arr))])