def minimalDist(graph: list,start: int)->list:
    visited = [False]*len(graph)
    dist = [float("inf")]*len(graph)
    dist[start] = 0
    nowVert = start
    for _ in range(vertexQ):
        visited[nowVert] = True
        for child in range(len(graph)):
            if graph[nowVert][child]!=-1 and (not visited[child]):
                if dist[child] > dist[nowVert]+graph[nowVert][child]:
                    dist[child] = dist[nowVert]+graph[nowVert][child]
        minDist = float("inf")
        for vert in range(len(graph)):
            if (not visited[vert]) and dist[vert]<minDist:
                minDist = dist[vert]
                nowVert = vert
    return dist
def whatRegion(distancesFromCapitals: list,city: int,capitals: list)->int:
    minDist,capital = float("inf"),-1
    for y in range(len(distancesFromCapitals)):
        if minDist>distancesFromCapitals[y][city]:
            minDist,capital = distancesFromCapitals[y][city],y
    if minDist!=float("inf"):
        return capitals[capital]
    return -1
capitals = list(map(int,input().split()))
vertexQ,edgeQ = capitals.pop(0),capitals.pop(0)
graph = [[-1 for _ in range(vertexQ)] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1][vertex2] = weight
    graph[vertex2][vertex1] = weight
distancesFromCapitals = [None for _ in range(len(capitals))]
for num,capital in enumerate(capitals):
    distancesFromCapitals[num] = minimalDist(graph,capital)
for city in range(vertexQ):
    print(whatRegion(distancesFromCapitals,city,capitals))

