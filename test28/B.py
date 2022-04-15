def iteration(graph,dist):
    for start in range(len(graph)):
        for child in graph[start]:
            dist[child[0]] = min([dist[child[0]],dist[start]+child[1]])


vertexQ, edgeQ, start = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
dist = [float("inf") for _ in range(vertexQ)]
dist[start] = 0
for _ in range(vertexQ-1):
    iteration(graph,dist)
lastDist = dist.copy()
for _ in range(vertexQ//2):
    iteration(graph,dist)
for i in range(vertexQ):
    if lastDist[i]>dist[i] or dist[i]==float("inf"):
        dist[i] = "UDF"
print(*dist)
