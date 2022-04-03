
def DFS(start: int,graph: list,colors: list,previous: list):
    colors[start] = 1
    for vert in graph[start]:
        previous[vert] = start
        if colors[vert] == 1:
            return vert,start
        elif colors[vert] == 0:
            return DFS(vert,graph,colors,previous)
    colors[start] = 2
vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
for i in range(vertexQ):
    colors,previous = [0 for _ in range(vertexQ)],[None for _ in range(vertexQ)]
    alpha = DFS(i,graph,colors,previous)
    if alpha!=None:
        cycleStart,cycleEnd = alpha
        cycle = []
        goThroughCycle = cycleEnd
        while goThroughCycle!=cycleStart:
            cycle.append(previous[goThroughCycle])
            goThroughCycle = previous[goThroughCycle]
        cycle.append(cycleEnd)
        print(*cycle[::-1])
        exit()
print("YES")

    
