def minPath(graph: list,start: int,end: int)->list:
    visited = [False]*len(graph)
    dist = [float("inf")]*len(graph)
    path = [None]*len(graph)
    dist[start] = 0
    nowVert = start
    for _ in range(vertexQ):
        visited[nowVert] = True
        for child in range(len(graph)):
            if graph[nowVert][child]!=-1 and (not visited[child]):
                if dist[child] > dist[nowVert]+graph[nowVert][child]:
                    dist[child] = dist[nowVert]+graph[nowVert][child]
                    path[child] = nowVert
        minDist = float("inf")
        for vert in range(len(graph)):
            if (not visited[vert]) and dist[vert]<minDist:
                minDist = dist[vert]
                nowVert = vert
    result = [end]
    while result[-1]!=start:
        result.append(path[result[-1]])
    return result[::-1]
    


vertexQ,edgeQ,start,end = map(int,input().split())
graph = [[-1 for _ in range(vertexQ)] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1][vertex2] = weight
    graph[vertex2][vertex1] = weight
print(*minPath(graph,start,end))
