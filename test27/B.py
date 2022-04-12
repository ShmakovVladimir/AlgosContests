def DFS(start,visited,graph):
    global compWeights
    visited[start] = True
    for vert in graph[start]:
        compWeights[-1] += vert[1]
        if not visited[vert[0]]:
            DFS(vert[0],visited,graph)
vertexQ, edqeQ = map(int, input().split())
graph = [[] for _ in range(vertexQ)]
compWeights = []
for _ in range(edqeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
    graph[vertex2].append([vertex1,weight])
visited = [False for _ in range(vertexQ)]
for start in range(vertexQ):
    if not visited[start]:
        compWeights.append(0)
        DFS(start,visited,graph)
for weight in sorted(compWeights):
    print(weight//2)