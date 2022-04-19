def minTree(graph: list,start: int)->list:
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
    return path

vertexQ,edgeQ = map(int,input().split())
graph = [[-1 for _ in range(vertexQ)] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1][vertex2] = weight
    graph[vertex2][vertex1] = weight
path = minTree(graph,0)
weight = 0
for i in range(1,vertexQ):
    weight+=graph[path[i]][i]
print(weight)
for i in range(1,vertexQ):
    print(str(path[i])+' '+str(i))




