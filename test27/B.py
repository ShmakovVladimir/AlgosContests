def DFS(start: int,visited: list,graph: list):
    global counter
    visited[start] = 1
    for vert in graph[start]:
        if visited[vert[0]]==0:
            counter+=vert[1]
            DFS(vert[0],visited,graph)
        elif visited[vert[0]]==1:
            counter+=2*vert[1]
    visited[start] = 2

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
    graph[vertex2].append([vertex1,weight])
visited = [False for _ in range(vertexQ)]
for i in range(vertexQ):
    if not visited[i]:
        counter = 0
        DFS(i,visited,graph)
        print((counter+2)//2-2)