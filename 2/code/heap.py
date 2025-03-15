def heapifiy(list,i,size): #checks the node to see if children are bigger, if bigger switch them and call again on switched node
    largest=i
    l=i*2+1
    r=i*2+2
    if(l<size and list[largest]<list[l]):
        largest=l
    if(r<size and list[largest]<list[r]):
        largest=r
    if(largest!=i):
        list[i],list[largest]=list[largest],list[i]
        heapifiy(list,largest,size) #largest is the original node after switching

def buildHeap(list): #builds the heap itself so we can sort(heap itself is not sorted it just contains the max at the root)
    size=len(list)
    for i in range(size//2,-1,-1):#we divide size by 2 to ignore the leaf nodes
        heapifiy(list,i,size)

def sort(list):
    for i in range(len(list)-1,0,-1):
        list[0], list[i] = list[i], list[0]
        heapifiy(list,0,i) #we use i because we decrease the size of the heap since we know that the last elements are sorted

arr=[1,4,5,7,43,6,9]
buildHeap(list)
sort(list)
print(list)

#sorting takes O(nlogn)
#building heap takes O(n)