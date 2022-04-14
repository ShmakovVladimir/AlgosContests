def DFS(start: int,visited: list,graph: list):
    global time,low,cutVertexes,timer
    visited[start] = True
    low[start] = time[start] = timer
    timer+=1
    for vert in graph[start]:
        if visited[vert]:
            low[start] = min(low[start],time[vert])
        elif not visited[vert]:
            DFS(vert,visited,graph)
            low[start] = min(low[start],low[vert])
            if low[vert]>=low[start] and start!=0:
                cutVertexes.append(start+1)

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1-1].append(vertex2-1)
    graph[vertex2-1].append(vertex1-1)
time,low = [0 for _ in range(vertexQ)],[float("inf") for _ in range(vertexQ)]
visited = [False for _ in range(vertexQ)]
cutVertexes,timer = [],0
if len(graph[0])>1:
    cutVertexes.append(1)
DFS(0,visited,graph)
if len(cutVertexes) == 0:
    print(-1)
    exit()
print(*sorted(cutVertexes))
