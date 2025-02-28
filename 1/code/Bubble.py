import time
def bubblesort(arr):
    begin = time.time()
    n = len(arr)
    for i in range(n-1):
        flag = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
                break

    end = time.time()
    total = end - begin
    print(f"the runtime of bubbleSort is {total} seconds")
