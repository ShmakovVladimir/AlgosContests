import queue

def BFS(start: int,visited: list,graph: list):
    steck = queue.Queue(0)
    steck.put(start)
    visited[start] = True
    dist,minCycle = [0 for _ in range(len(graph))],[]
    path,minCycleLength = [None for _ in range(len(graph))],float("inf")
    while not steck.empty():
        vert = steck.get()
        for neib in graph[vert]:
            if not visited[neib]:
                steck.put(neib)
                visited[neib] = True
                dist[neib] = dist[vert]+1
                path[neib] = vert
            else:
                cycleLength = dist[vert]-dist[neib]
                if cycleLength<minCycleLength and cycleLength>2:
                    minCycleLength = cycleLength
                    minCycle = []
                    minCycle.append(vert)
                    for _ in range(cycleLength):
                        minCycle.append(path[minCycle[-1]])
    return minCycle

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
visited = [False for _ in range(vertexQ)]
minCycle = [None]*(vertexQ+2)
for i in range(vertexQ):
    if not visited[i]:
        alpha = BFS(i,visited,graph)
        if len(alpha)>0 and len(alpha)<len(minCycle):
            minCycle = alpha
if len(minCycle)!=vertexQ+2:
    print(*minCycle[::-1])
    exit()
print("NO CYCLES")

                


                

