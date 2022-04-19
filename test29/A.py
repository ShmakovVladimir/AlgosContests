import queue

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)
visited = [False for _ in range(vertexQ)]
steck = queue.Queue(0)
tree = []
steck.put(0)
visited[0] = True
while not steck.empty():
    vertStart = steck.get()
    for neib in graph[vertStart]:
        if not visited[neib]:
            steck.put(neib)
            visited[neib] = True
            tree.append([vertStart,neib])
for i in tree:
    print(str(i[0])+' '+str(i[1]))
