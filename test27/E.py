import queue

def BFS(start: int,visited: list,graph: list):
    steck = queue.Queue(0)
    steck.put(start)
    visited[start] = True
    while not steck.empty():
        vert = steck.get()
        for neib in graph[vert]:
            if not visited[neib]:
                steck.put(neib)
                visited[neib] = True

def countConnectivitys(graph: list,doNotVisit: int):
    global visited
    ans = 0
    visited[doNotVisit] = True
    for i in range(len(graph)):
        if not visited[i]:
            BFS(i,visited,graph)
            ans +=1
    return ans

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
if vertexQ==1:
    print(-1)
for _ in range(edgeQ):
    sVertex,eVertex = map(int,input().split())
    graph[sVertex-1].append(eVertex-1)
    graph[eVertex-1].append(sVertex-1)
res = []
visited = [False]*len(graph)
for i in range(vertexQ):
    if countConnectivitys(graph,i)-1:
        res.append(i+1)
if len(res)==0:
    print(-1)
    exit()
print(*res)

