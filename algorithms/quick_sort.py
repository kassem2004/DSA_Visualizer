import time
def partition(arr, l, h, draw_bars, speed):
    pivot = arr[h]

    i = l - 1

    for j in range(l, h + 1):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
            draw_bars(arr, ["red" if x == i or x == j else "yellow" if l <= x <= h else "blue" for x in range(len(arr))])
            time.sleep(speed)
    return i


def quick(arr, l, h, draw_bars, speed):
    if l < h:
        p = partition(arr, l, h, draw_bars=draw_bars, speed=speed)

        quick(arr, l, p - 1, draw_bars=draw_bars, speed=speed)
        quick(arr, p + 1, h, draw_bars=draw_bars, speed=speed)
        draw_bars(arr, ["green" if x <= p else "blue" for x in range(len(arr))])
        time.sleep(speed)