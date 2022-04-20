import heapq

def binDeikstra(graph: list,start: int,end: int)->list:
    heap = []
    visited = [False for _ in range(len(graph))]
    dist = [float("inf") for _ in range(len(graph))]
    dist[start] = 0
    path = [None for _ in range(len(graph))]
    heapq.heappush(heap,(0,start))
    while len(heap)>0:
        nowVert = heapq.heappop(heap)[1]
        visited[nowVert] = True
        for neib in graph[nowVert]:
            if  dist[neib[0]] > dist[nowVert]+neib[1] and (not visited[neib[0]]):
                dist[neib[0]] = dist[nowVert]+neib[1]
                heapq.heappush(heap,(dist[neib[0]],neib[0]))
                path[neib[0]] = nowVert
    if dist[end] == float("inf"):
        return [-1]
    result = [end]
    while result[-1]!=start:
        result.append(path[result[-1]])
    result = result[::-1]
    for i in range(len(result)):
        if i%2==1:
            result[i]-=1
        result[i]//=2
    return result

vertexQ,edgeQ = map(int,input().split())
graph = [[] for _ in range(2*vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2,weight = map(int,input().split())
    graph[2*vertex1+1].append([2*vertex2,weight])
    graph[2*vertex2].append([2*vertex1+1,weight])
    graph[2*vertex2+1].append([2*vertex1,weight])
    graph[2*vertex1].append([2*vertex2+1,weight])
ans = []
for _ in range(int(input())):
    start,end = map(int,input().split())
    ans.append(binDeikstra(graph,start*2,end*2))
for line in ans:
    print(*line)

