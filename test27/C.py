
def DFS(start: int,colors: list,graph: list,cycle: list):
    colors[start] = 1
    cycle.append(start)
    for vert in graph[start]:
        if colors[vert] == 1:
            return cycle
        elif colors[vert] == 0:
            DFS(vert,colors,graph,cycle)
    colors[start] = 2
    cycle.pop()

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1-1].append(vertex2-1)
for i in range(vertexQ):
    colors = [0 for _ in range(vertexQ)]
    alpha = DFS(i,colors,graph,[])
    
    print(alpha)
   
print("YES")