from quick import part
def getKthElement(list, index, start=0, end=None):
    if end is None:
        end = len(list) - 1
    i=part(list,start,end)
    if(i==index-1): print(list[i])
    elif(i>index-1):getKthElement(list,index,start,i-1)
    else: getKthElement(list,index,i+1,end)

list=[1,4,5,7,43,6,9]
getKthElement(list,5)
