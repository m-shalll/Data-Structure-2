import time
def insertionSort(nums):
    begin = time.time()
    n=len(nums)
    if n<=1:
        return
    for i in range(1,n):
        current=nums[i]
        previous=i-1
        while(previous >= 0 and current<nums[previous]):
            nums[previous+1]=nums[previous]
            previous-=1
        nums[previous+1]=current
    end = time.time() 
    total=end-begin
    return total

arr = [12, 11, 13, 5, 6]
total=insertionSort(arr)
print(arr)
print(total)