from H_Insertion import insertionSort
from merge import merge

def hybrid_sort(arr, first, last, threshold):
    if (last - first + 1) <= threshold:
        insertionSort(arr, first, last)
        return
    if first < last:
        mid = (first + last) // 2
        hybrid_sort(arr, first, mid, threshold)
        hybrid_sort(arr, mid + 1, last, threshold)
        merge(arr, first, mid, last)

arr=[1,4,5,7,43,6,9]
hybrid_sort(arr, 0, len(arr) - 1, 3)
print(arr)
