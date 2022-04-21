import queue

def minimalDist(graph: list,start: int)->list:
    heap = queue.LifoQueue(0)
    visited = [False for _ in range(len(graph))]
    heap.put((0,start))
    while not heap.empty():
        nowVert = heap.get()[1]
        visited[nowVert] = True
        for neib in graph[nowVert]:
            if  (not isCapital[neib[0]]) and (not visited[neib[0]]) and distancesandPaths[neib[0]][0] > distancesandPaths[nowVert][0]+neib[1]:
                distancesandPaths[neib[0]][0] = distancesandPaths[nowVert][0]+neib[1]
                distancesandPaths[neib[0]][1] = start
                heap.put((distancesandPaths[neib[0]][0],neib[0]))


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
    minimalDist(graph,capital)
for i in distancesandPaths:
    print(i[1])
