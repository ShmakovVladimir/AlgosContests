
class Network:
    class edge:
        def __init__(self,vertexFrom: int,vertexTo: int,capasity: int):
            self.vertexFrom,self.vertexTo,self.capasity = vertexFrom,vertexTo,capasity
        def __eq__(self,other)->bool:
            return (self.vertexFrom == other.vertexFrom and self.vertexTo == other.vertexTo) 
        def __hash__(self):
            return (self.vertexFrom+self.vertexTo)*(self.vertexFrom+self.vertexTo+1)//2 + self.vertexFrom
    def __init__(self):
        self.readGraph()
        self.stock,self.source = self.vertexQ-1,0
        self.restNetwork = self.graph.copy()
    def findMaxFlow(self)->int:
        path = self.findPath()
        minCap = self.findMinCapasity(path)
        flow = 0
        while bool(path):
            for vertNumber in range(len(path)-1):
                vertex1,vertex2 = path[vertNumber],path[vertNumber+1]
                flow+=minCap
                self.matrix[vertex1][vertex2] -= minCap
                self.matrix[vertex2][vertex1] += minCap
                self.restNetwork[vertex1].add(self.edge(vertex1,vertex2,self.matrix[vertex1][vertex2]))
                self.restNetwork[vertex2].add(self.edge(vertex2,vertex1,self.matrix[vertex2][vertex1]))
            path = self.findPath()
            minCap = self.findMinCapasity(path)
        return flow
    def readGraph(self):
        self.vertexQ,self.edgeQ = map(int,input().split())
        self.graph = [set() for _ in range(self.vertexQ)]
        self.matrix = [[None for _ in range(self.vertexQ)] for _ in range(self.vertexQ)]
        for _ in range(self.edgeQ):
            vertex1,vertex2,capasity =  map(int,input().split())
            self.graph[vertex1].add(self.edge(vertex1,vertex2,capasity))
            self.matrix[vertex1][vertex2] = capasity
            self.matrix[vertex2][vertex1] = 0
    def findPath(self)->list:
        def DFS(start: int,graph: list,path: list,visited: list):
            visited[start] = False
            for neib in graph[start]:
                if not visited[neib.vertexTo] and neib.capasity>0:
                    path[neib.vertexTo] = start
                    DFS(neib.vertexTo,graph,path,visited)
        whereAreYouFrom = [None for _ in range(self.vertexQ)]
        visited = [False for _ in range(self.vertexQ)]
        DFS(self.source,self.restNetwork,whereAreYouFrom,visited)
        if whereAreYouFrom[self.stock] is None:
            return False
        path = [self.stock]
        while path[-1]!=self.source:
            path.append(whereAreYouFrom[path[-1]])
        return path
    def findMinCapasity(self,path: list)->int:
        minCap = float("inf")
        for vertNumber in range(len(path)-1):
                vertex1,vertex2 = path[vertNumber],path[vertNumber+1]
                minCap = min(self.matrix[vertex1][vertex2],minCap)
        return minCap

network = Network()
print(network.findMaxFlow())