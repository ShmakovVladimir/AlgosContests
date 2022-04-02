
def DFS(start: int,visited: list,graph: list):
    visited[start] = True 
    for i in graph[start]:
        if not visited[i]:  DFS(i,visited,graph)
vertexQ,edgeQ = int(input()),int(input())
graph = [[] for _ in range(vertexQ)]
visited = [False for _ in range(vertexQ)]
for _ in range(edgeQ):
    sVertex,eVertex = map(int,input().split())
    graph[sVertex].append(eVertex)
    graph[eVertex].append(sVertex)
DFS(0,visited,graph)
if sum(visited) == len(visited):
    print("YES")
    exit()
print("NO")
