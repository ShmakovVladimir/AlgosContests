def findSmallest(arr,start) ->int:
    min,minIndex = float("+inf"),0
    for i in range(start,len(arr)):
        if min>arr[i]:
            min,minIndex = arr[i],i 
    return minIndex
def choiseSort(arr,index = 0):
    if index==len(arr):
        return
    minIndex = findSmallest(arr,index)
    if index!=minIndex:
        arr[index],arr[minIndex] = arr[minIndex],arr[index]
        print(*arr)
    choiseSort(arr,index+1)
choiseSort([int(i) for i in input().split()])
