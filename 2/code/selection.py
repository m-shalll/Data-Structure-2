import time
def selectionSort(arr):
    begin = time.time()
    n = len(arr)
    for i in range (n-1):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[j], arr[minimum] = arr[minimum], arr[j]
    end = time.time()
    total = end - begin
    return total