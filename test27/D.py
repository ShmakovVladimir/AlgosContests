def cycleDFS(start: int,graph: list,colors: list,previous: list):
    colors[start] = 1
    for vert in graph[start]:
        if colors[vert]==0:
            previous[vert] = start
            if cycleDFS(vert,graph,colors,previous):
                return True
        elif colors[vert]==1:
            return True
    colors[start] = 2
    return False
def DFS(start: int,topSort: list,visited: list,graph: list):
    visited[start] = True
    for vert in graph[start]:
        if not visited[vert]:
            DFS(vert,topSort,visited,graph)
    topSort.append(start)
vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
colors = [0 for _ in range(vertexQ)]
for i in range(vertexQ):
    if colors[i]!=2:
        if cycleDFS(i,graph,colors,[None for _ in range(vertexQ)]):
            print("NO")
            exit()
visited,topSort = [False for _ in range(vertexQ)],[]
for i in range(vertexQ):
    if not visited[i]:
        DFS(i,topSort,visited,graph)
print(*topSort[::-1])