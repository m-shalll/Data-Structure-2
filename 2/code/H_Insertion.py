import time
def insertionSort(nums,first,last):
    n=last-first+1
    if n<=1:
        return
    for i in range(first+1,last+1):
        current=nums[i]
        previous=i-1
        while(previous >= first and current<nums[previous]):
            nums[previous+1]=nums[previous]
            previous-=1
        nums[previous+1]=current