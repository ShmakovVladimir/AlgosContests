
def DFS(start: int,visited: list,graph: list):
    global weightCounter
    visited[start] = True 
    for i in graph[start]:
        if not visited[i[0]]:  
            weightCounter+=i[1]
            DFS(i[0],visited,graph)
vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
    graph[vertex2].append([vertex1,weight])
visited = [False for _ in range(vertexQ)]
for i in range(vertexQ):
    if not visited[i]:
        weightCounter = 0
        DFS(i,visited,graph)
        print(weightCounter)
        
