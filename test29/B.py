vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[vertex1].append([vertex2,weight])
    graph[vertex2].append([vertex1,weight])
visited = [False]*vertexQ
dist = [float("inf") for _ in range(vertexQ)]
path = [None for _ in range(vertexQ)]
nowVert = 0
visited[nowVert] = True
dist[nowVert] = 0
treeLength,tree = 0,[]
for _ in range(vertexQ-1):
    for child in graph[nowVert]:
        if (not visited[child[0]]) and dist[child[0]] > child[1]:
            dist[child[0]] = child[1]
            path[child[0]] = nowVert
    minInd,minDist = None,float("inf")
    for i in range(vertexQ):
        if minDist>dist[i] and (not visited[i]):
            minDist = dist[i]
            minInd = i
    treeLength+=minDist
    tree.append([path[minInd],minInd])
    nowVert = minInd
    visited[minInd] = True
print(treeLength)
for i in tree:
    print(str(i[0])+' '+str(i[1]))


