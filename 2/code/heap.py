def heapifiy(arr,i,size): #checks the node to see if children are bigger, if bigger switch them and call again on switched node
    largest=i
    l=i*2+1
    r=i*2+2
    if(l<size and arr[largest]<arr[l]):
        largest=l
    if(r<size and arr[largest]<arr[r]):
        largest=r
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        heapifiy(arr,largest,size) #largest is the original node after switching

def buildHeap(arr): #builds the heap itself so we can sort(heap itself is not sorted it just contains the max at the root)
    size=len(arr)
    for i in range(size//2,-1,-1):#we divide size by 2 to ignore the leaf nodes
        heapifiy(arr,i,size)

def heap_sort(arr):
    for i in range(len(arr)-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapifiy(arr,0,i) #we use i because we decrease the size of the heap since we know that the last elements are sorted

#sorting takes O(nlogn)
#building heap takes O(n)