
def DFS(start:int ,colors: list,graph: list,FLAG: bool):
    colors[start] = 1
    for vert in graph[start]:
        if colors[vert] == 1:
           FLAG = True
        elif colors[vert] == 0:
            DFS(vert,colors,graph,FLAG)
    colors[start] = 2
vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    sVertex,eVertex = map(int,input().split())
    graph[sVertex].append(eVertex)
colors = [0 for _ in range(vertexQ)]
for i in range(vertexQ):
        FLAG = False
        DFS(i,colors,graph,FLAG)
        print(FLAG)