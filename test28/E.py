def childs(heap: list,index: int) -> tuple:
    if len(heap)>2*index+2:
        return heap[index*2+1][0],heap[index*2+2][0]
    elif len(heap)>2*index+1:
        return heap[index*2+1][0],float('inf')
    return float('inf'),float('inf')
def minChildIndex(heap: list,index: int) -> int:
    if heap[2*index+1][0] == min(childs(heap,index)):
        return 2*index+1
    return 2*index+2
def perc(heap: list,ind: int) -> None:
    while 2*ind<=len(heap):
        if heap[ind][0]>min(childs(heap,ind)):
            alpha = minChildIndex(heap,ind)
            heap[ind][0],heap[minChildIndex(heap,ind)] = heap[minChildIndex(heap,ind)][0],heap[ind][0]
            ind = alpha
        else:
            break
def buildHeapLinearTime(heap: list):
    for i in range(len(heap),-1,-1):
        perc(heap,i)
def popHeap(heap: list):
    ans = heap.pop()
    perc(heap,0)
    return ans 
def heapPut(heap: list,element):
    heap.append(element)
    heap[0],heap[-1] = heap[-1],heap[0]
    perc(heap,0)
def minimalDist(graph: list,start: int)->list:
    heap = []
    visited = [False for _ in range(len(graph))]
    dist = [float("inf") for _ in range(len(graph))]
    dist[start] = 0
    heap.append((0,start))
    while len(heap)>0:
        nowVert = popHeap(heap)
        visited[nowVert] = True
        for neib in graph[nowVert]:
            if  dist[neib[0]] > dist[nowVert]+neib[1] and (not visited[neib[0]]):
                dist[neib[0]] = dist[nowVert]+neib[1]
                heapPut(heap,(dist[neib[0]],neib[0]))
    return dist

capitals = list(map(int,input().split()))
vertexQ,edgeQ = capitals.pop(0),capitals.pop(0)
graph = [[] for _ in range(vertexQ)]
isCapital = [False for _ in range(vertexQ)]
for cap in capitals:
    isCapital[cap] = True
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
    graph[vertex2].append([vertex1,weight])

distancesandPaths = [[float("inf"),-1] for _ in range(vertexQ)]
for i in range(vertexQ):
    if isCapital[i]:
        distancesandPaths[i] = [0,i]
for capital in capitals:
    distFromCap = minimalDist(graph,capital)
    for i in range(vertexQ):
        if distFromCap[i]<distancesandPaths[i][0] and (not isCapital[i]):
            distancesandPaths[i][0] = distFromCap[i]
            distancesandPaths[i][1] = capital
for i in distancesandPaths:
    print(i[1])
