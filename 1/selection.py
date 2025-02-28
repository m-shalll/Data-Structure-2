def selectionSort(arr, n):
    for i in range (n-1):
        min = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min]:
                min = j
        arr[j], arr[min] = arr[min], arr[j]
        