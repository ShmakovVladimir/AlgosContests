def DFS(start: int,graph: list,colors: list,previous: list):
    global cycleEnd,cycleStart
    colors[start] = 1
    for vert in graph[start]:
        if colors[vert]==0:
            previous[vert] = start
            if DFS(vert,graph,colors,previous):
                return True
        elif colors[vert]==1:
            cycleEnd = start
            cycleStart = vert
            return True
    colors[start] = 2
    return False
vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
colors,previous = [0 for _ in range(vertexQ)],[None for _ in range(vertexQ)]
minCycle = [None]*(vertexQ+1)
for i in range(vertexQ):
    cycleStart,cycleEnd = None,None
    if colors[i]!=2:
         if DFS(i,graph,colors,previous):
            cycle = []
            goThroughCycle = cycleEnd
            while goThroughCycle!=cycleStart:
                cycle.append(previous[goThroughCycle])
                goThroughCycle = previous[goThroughCycle]
            cycle.append(cycleEnd)
            if len(minCycle)>len(cycle):
                minCycle = cycle


if len(minCycle)==vertexQ+1:
    print("NO CYCLES")
    exit()
print(minCycle)          