def children(heap: list,heapLength: int,ind: int)->tuple:
    if heapLength>ind*2+2:
        return heap[ind*2+1],heap[ind*2+2]
    if heapLength>ind*2+1:
        return heap[ind*2+1],float('-inf')
    return float('-inf'),float('-inf')
def siftDown(heap: list,heapLength: int,ind: int)->None:
    while 2*ind<=heapLength:
        if max(children(heap,heapLength,ind))>heap[ind]:
            if heap[ind*2+1]==max(children(heap,heapLength,ind)):
                heap[ind],heap[ind*2+1] = heap[ind*2+1],heap[ind]
                ind = ind*2+1
            else:
                heap[ind*2+2],heap[ind] = heap[ind],heap[ind*2+2]
                ind = ind*2+2
        else:
            break
def buildMaxHeap(arr: list):
    for i in range(len(arr)//2,-1,-1):
        siftDown(arr,len(arr),i)
def heapsort(arr: list):
    buildMaxHeap(arr)
    print(*arr)
    for heapLength in range(len(arr)-1,0,-1):
        arr[heapLength],arr[0] = arr[0],arr[heapLength]
        siftDown(arr,heapLength,0)
        print(*arr)