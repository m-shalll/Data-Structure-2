from Bubble import bubblesort
from Insertion import insertionSort
from selection import selectionSort
import random
import matplotlib.pyplot as plt
import numpy as np
def randomArrayGenerator(size):
    return [random.randint(0,100000) for _ in range(size)]

arr_sizes = [1000, 25000, 50000, 75000]
n = len(arr_sizes)
bubble_ypoints = np.empty(n)
insertion_ypoints = np.empty(n)
selection_ypoints = np.empty(n)
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
plt.xlabel("Array size")
plt.ylabel("Time in seconds")
plt.plot(xpoints,  bubble_ypoints, label="Bubble Sort", marker="o")
plt.plot(xpoints, insertion_ypoints, label="Insertion Sort", marker="s")
plt.plot(xpoints, selection_ypoints, label="Selection Sort", marker="s")
plt.legend()
plt.show()