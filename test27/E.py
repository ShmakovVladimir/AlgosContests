
vertexQ,edgeQ = map(int,input().split())
graph = [[0 for _ in range(vertexQ)] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1-1][vertex2-1],graph[vertex2-1][vertex1-1] = 1,1
sources = []
for j in range(len(graph)):
    sigma = 0
    for k in range(len(graph)):
        sigma+=graph[k][j]
    if sigma == 0:
        sources.append(j+1)
print(*sources)

