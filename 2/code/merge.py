def merge(arr, first, mid, last):
    temp = [0] * (last + 1)
    first1 = first
    last1 = mid
    first2 = mid + 1
    last2 = last
    i = first1
    while first1 <= last1 and first2 <= last2:
        if arr[first1] < arr[first2]:
            temp[i] = arr[first1]
            first1 += 1
        else:
            temp[i] = arr[first2]
            first2 += 1
        i += 1
    while first1 <= last1:
        temp[i] = arr[first1]
        first1 += 1
        i += 1
    while first2 <= last2:
        temp[i] = arr[first2]
        first2 += 1
        i += 1
    i = first
    while i <= last:
        arr[i] = temp[i]
        i += 1

def merge_sort(arr, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        merge(arr, first, mid, last)
