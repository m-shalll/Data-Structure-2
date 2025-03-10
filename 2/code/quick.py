def quicksort(arr, start, end):
    if end <= start: return # array cannot be divided anymore
    pivot = part(arr, start, end)
    quicksort(arr, start, pivot-1) #left partition
    quicksort(arr, pivot+1, end) #right partition

def part(arr, start, end):
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] < pivot:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
    i=i+1
    arr[i], arr[end] = arr[end], arr[i]
    return i
