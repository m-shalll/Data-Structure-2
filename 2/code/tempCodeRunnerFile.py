from Bubble import bubblesort
from Insertion import insertionSort
from selection import selectionSort
from heap import heap_sort
from hybrid import hybrid_sort
from merge import merge_sort
import random
import matplotlib.pyplot as plt
import numpy as np
import time
def randomArrayGenerator(size):
    return [random.randint(0,100000) for _ in range(size)]


arr_sizes = [1000]
n = len(arr_sizes)
bubble_ypoints = np.empty(n)
insertion_ypoints = np.empty(n)
selection_ypoints = np.empty(n)
heap_ypoints = np.empty(n)
hybrid_ypoints = np.empty(n)
merge_ypoints = np.empty(n)
xpoints = np.array(arr_sizes)
for i in range(n):
    testArray = randomArrayGenerator(arr_sizes[i])
    bubble_time = bubblesort(testArray.copy())
    insertion_time = insertionSort(testArray.copy())
    selection_time = selectionSort(testArray.copy())
    print(f"the runtime of bubbleSort is {bubble_time} seconds")
    print(f"the runtime of insertionSort is {insertion_time} seconds")
    print(f"the runtime of selectionSort is {selection_time} seconds")
    bubble_ypoints[i] = bubble_time
    insertion_ypoints[i] = insertion_time
    selection_ypoints[i] = selection_time

    begin = time.time()
    heap_sort(testArray.copy())
    end = time.time()
    heap_ypoints[i] = end - begin
    begin = time.time()
    hybrid_sort(testArray.copy(),0,len(testArray.copy())-1,7)
    end = time.time()
    hybrid_ypoints[i] = end-begin
    begin = time.time()
    merge_sort(testArray.copy(),0,len(testArray.copy())-1)
    end = time.time()
    merge_ypoints[i] = end-begin
plt.xlabel("Array size")
plt.ylabel("Time in seconds")
plt.plot(xpoints,  bubble_ypoints, label="Bubble Sort", marker="o")
plt.plot(xpoints, insertion_ypoints, label="Insertion Sort", marker="s")
plt.plot(xpoints, selection_ypoints, label="Selection Sort", marker="s")
plt.plot(xpoints,  heap_ypoints, label="Heap Sort", marker="o")
plt.plot(xpoints, hybrid_ypoints, label="Hybrid Sort", marker="s")
plt.plot(xpoints, merge_ypoints, label="Merge Sort", marker="s")
plt.legend()
plt.show()