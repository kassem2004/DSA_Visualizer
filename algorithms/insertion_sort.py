import time
def insertion(arr, draw_bars, speed):
    for i in range(1, len(arr)):
        cmp = arr[i]
        j = i - 1

        while j >=0 and arr[j] > cmp:
            arr[j + 1] = arr[j]
            j -=1
            draw_bars(arr, ["red" if x == i else "yellow" if x == j else "blue" for x in range(len(arr))])
            time.sleep(speed)
        arr[j + 1] = cmp