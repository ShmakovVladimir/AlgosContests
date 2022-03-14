def childs(heap: list,index: int) -> tuple:
    if len(heap)>2*index+2:
        return heap[index*2+1],heap[index*2+2]
    elif len(heap)>2*index+1:
        return heap[index*2+1],float('inf')
    return float('inf'),float('inf')
def minChildIndex(heap: list,index: int) -> int:
    if heap[2*index+1] == min(childs(heap,index)):
        return 2*index+1
    return 2*index+2
def perc(heap: list,ind: int) -> None:
    while 2*ind<=len(heap):
        if heap[ind]>min(childs(heap,ind)):
            alpha = minChildIndex(heap,ind)
            heap[ind],heap[minChildIndex(heap,ind)] = heap[minChildIndex(heap,ind)],heap[ind]
            ind = alpha
        else:
            break
def buildHeapLinearTime(heap: list):
    for i in range(len(heap),-1,-1):
        perc(heap,i)
_,heap = input(),[int(i) for i in input().split()]
buildHeapLinearTime(heap)
print(*heap)