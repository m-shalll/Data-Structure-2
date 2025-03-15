import random


def quicksort(arr, start, end):
    if start < end:
        pivot_index = random_part(arr, start, end)
        quicksort(arr, start, pivot_index-1)
        quicksort(arr, pivot_index + 1, end)

def random_part(arr, start, end):
    rand_pivot = random.randint(start, end)
    arr[start], arr[rand_pivot] = arr[rand_pivot], arr[start]
    return partition(arr, start, end)

def partition(arr, start, end):
    pivot = start
    i = start+1
    for j in range(start+1,end+1):
        if arr[j] <= arr[pivot]:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
    arr[i-1], arr[pivot] = arr[pivot], arr[i-1]
    pivot = i-1
    return pivot