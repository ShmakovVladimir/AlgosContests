import queue


vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)
steck,visited = queue.Queue(0),[True]+[False for _ in range(vertexQ-1)]
dist = [0 for _ in range(vertexQ)]
steck.put(0)
while not steck.empty():
    vert = steck.get()
    for neib in graph[vert]:
        if not visited[neib]:
            steck.put(neib)
            dist[neib] = dist[vert]+1
            visited[neib] = True
for i in dist:
    print(i)



