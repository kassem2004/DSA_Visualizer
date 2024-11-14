import time
def merge(arr, l, m, r, draw_bars, speed):
    n1 = m - l + 1
    n2 = r - m
    left_arr = [0] * n1
    right_arr = [0] * n2
    for i in range(n1):
        left_arr[i] = arr[l + i]
    for i in range(n2):
        right_arr[i] = arr[m + i + 1]

    i = 0
    j = 0
    k = l

    draw_bars(arr, ["yellow" if l <= x <= r else "blue" for x in range(len(arr))])
    time.sleep(speed)
    
    while i < n1 and j < n2:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    draw_bars(arr, ["yellow" if l <= x <= r else "blue" for x in range(len(arr))])
    time.sleep(speed)
    
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1
    draw_bars(arr, ["yellow" if l <= x <= r else "blue" for x in range(len(arr))])
    time.sleep(speed)



def merge_sort(arr, l, r, draw_bars, speed):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m, draw_bars=draw_bars, speed=speed)
        merge_sort(arr, m + 1, r, draw_bars=draw_bars, speed=speed)
        merge(arr, l, m, r, draw_bars=draw_bars, speed=speed)
        draw_bars(arr, ["green" if l <= x <= r else "blue" for x in range(len(arr))])
        time.sleep(speed)