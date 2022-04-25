class Network:
    class Edge:
        def __init__(self,vertexFrom: int,vertexTo: int,capasity: int):
            self.vertexFrom, self.vertexTo = vertexFrom, vertexTo
            self.capasity = capasity
            self.invertEdge = None
    def __init__(self):
        self.readGraph()
        self.source,self.stock = 0,self.vertexQ-1
    def findMaxFlow(self):
        maxFlow = 0
        while self.findPathAndCapasity():
            maxFlow+=self.minCapasity
            for edge in self.edgesInPath:
                edge.capasity-=self.minCapasity
                edge.invertEdge.capasity+=self.minCapasity
        if maxFlow>=self.K:
            print("YES")
            return
        print("NO")
    def readGraph(self):
        self.vertexQ,self.edgeQ, self.K = map(int,input().split())
        self.networkEdges = [[] for _ in range(self.vertexQ)]
        for _ in range(self.edgeQ):
            vertex1,vertex2 = map(int,input().split())
            capasity = 1 
            self.networkEdges[vertex1].append(self.Edge(vertex1,vertex2,capasity))
            self.networkEdges[vertex2].append(self.Edge(vertex2,vertex1,0))
            self.networkEdges[vertex1][-1].invertEdge = self.networkEdges[vertex2][-1]
            self.networkEdges[vertex2][-1].invertEdge = self.networkEdges[vertex1][-1]
    def findPathAndCapasity(self):
        def DFS(start: int):
            visited[start] = True
            for edge in self.networkEdges[start]:
                if (not visited[edge.vertexTo]) and edge.capasity:
                    previousInPath[edge.vertexTo] = start
                    capasitys[edge.vertexTo] = edge.capasity
                    edgeToVertex[edge.vertexTo] = edge
                    DFS(edge.vertexTo)
        previousInPath = [None for _ in range(self.vertexQ)]
        visited = [False for _ in range(self.vertexQ)]
        capasitys = [None for _ in range(self.vertexQ)]
        edgeToVertex = [None for _ in range(self.vertexQ)]
        DFS(self.source)
        if not visited[self.stock]:
            return False
        self.path = [self.stock]
        self.edgesInPath = []
        self.minCapasity = float("inf")
        while self.path[-1] != self.source:
            self.minCapasity = min(self.minCapasity,capasitys[self.path[-1]])
            self.edgesInPath.append(edgeToVertex[self.path[-1]])
            self.path.append(previousInPath[self.path[-1]])
        return True
alpha = Network()
alpha.findMaxFlow()
