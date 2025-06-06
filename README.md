# ✅Assignment 1:
For our first assignment, we have been asked to create the following algorithms:

- Bubble sort: This sorting technique keeps comparing adjacent elements and swapping their places, resulting in the maximum or minimum element moving to the end of the list.
  
- Selection sort: In contrast with bubble sort, selection sort does not change the position of adjacent elements; however, it finds the smallest or biggest element and swaps it with the element in its correct position.

- Insertion sort: This algorithm divides the dataset into two parts — one sorted and one unsorted. During each pass, an element from the unsorted part is inserted into the sorted part until the unsorted part is empty.

What is common between these sorting algorithms is that their worst-case scenario is **O(n<sup>2</sup>)**. However, the best-case scenario occurs when the lists are already ordered, making the best-case time complexity for bubble and insertion sort **O(n)**. Due to the nature of insertion sort, fewer comparisons are made compared to the other two algorithms, making it faster for small datasets and requiring less running time.

---

# ✅Assignment 2:
Following the previous assignment, we were asked to implement other sorting algorithms that are much faster and solve a simple yet tricky problem:

- ⚓Quick sort: a divide and conquer algorithm where we pick a pivot in our list and we sort to so that all the elements that are on the left of the pivot are smaller and all the elements on right are bigger and we repeat this process with different pivots.
  
- ➗Merge sort: an also a divide and conquer algorithm, which keeps recursively dividing the list on halves, sort each half seperately and then merging the sorted halves.
  
- 🌲Heap sort: this sorting algorithm contains multiple steps:
  1.Building heap: a heap is a nearly complete binary tree, there can be a max or a min heap, a max heap has the largest element in its root, and every child is smaller than its parent(apply same logic to min heap).
  2.Heapify: it is the process where we place a node(element) in its correct position in the tree, this happens by comparing the node with its children and switch their positions, then apply heapify again to the same node but in its new position until it is placed in its correct place.
  3.Sorting: the sorting itself happens by removing the root, placing the last element in the root, heapifiy to fix the heap and repeating this process.
     
- Hybrid merge and insertion sort:


Find kth smallest

---
