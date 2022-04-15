def minimalDist(graph: list,start: int,end: int)->list:
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

vertexQ,edgeQ = map(int,input().split())
graph = [[-1 for _ in range(vertexQ)] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1][vertex2] = weight
    graph[vertex2][vertex1] = weight
minDist,capital = float("inf"),0
for vert in range(vertexQ):
    alpha = sum(minimalDist(graph,vert,0))
    if alpha<minDist:
        capital = vert
        minDist = alpha
print(capital)
