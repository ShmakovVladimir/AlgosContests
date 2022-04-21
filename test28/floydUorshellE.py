


capitals = list(map(int,input().split()))
vertexQ,edgeQ = capitals.pop(0),capitals.pop(0)
graph = [[float("inf") for _ in range(vertexQ)] for _ in range(vertexQ)]
isCapital = [False for _ in range(vertexQ)]
for cap in capitals:
    isCapital[cap] = True
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1][vertex2] = weight
    graph[vertex2][vertex1] = weight
path = [-1 for _ in range(vertexQ)]
for cap in range(vertexQ):
    for i in capitals:
        for j in range(vertexQ):
            if graph[i][j]>graph[i][cap]+graph[cap][j]:
                graph[i][j] = graph[i][cap]+graph[cap][j]
                path[cap] = i

for i in path:
    print(i)

