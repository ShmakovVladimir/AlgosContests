import heapq

def binDeikstra(graph: list,start: int)->list:
    heap = []
    visited = [False for _ in range(len(graph))]
    dist = [float("inf") for _ in range(len(graph))]
    dist[start] = 0
    heapq.heappush(heap,(0,start))
    while len(heap)>0:
        nowVert = heapq.heappop(heap)[1]
        visited[nowVert] = True
        for neib in graph[nowVert]:
            if  dist[neib[0]] > dist[nowVert]+neib[1] and (not visited[neib[0]]):
                dist[neib[0]] = dist[nowVert]+neib[1]
                heapq.heappush(heap,(dist[neib[0]],neib[0]))

    return dist

capitals = list(map(int,input().split()))
vertexQ,edgeQ = capitals.pop(0),capitals.pop(0)
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
    graph[vertex2].append([vertex1,weight])
distancesFromCapitals = [None for _ in range(len(capitals))]
for vert in range(len(capitals)):
    distancesFromCapitals[vert] = binDeikstra(graph,capitals[vert])
for city in range(vertexQ):
    minDist,minCapital = float("inf"),-1
    for capital in range(len(capitals)):
        if distancesFromCapitals[capital][city]<minDist:
            minDist = distancesFromCapitals[capital][city]
            minCapital = capital
    print(minCapital)


