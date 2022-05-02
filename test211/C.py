class State:
    def __init__(self):
        self.win = None
        self.visits = 0
        self.edgesFrom = 0
    def definedState(self)->bool:
        return self.win is not None

def DFS(start: int):
    global invertedGraph,states
    for neib in invertedGraph[start]:
        if not states[neib].definedState():
            if states[start].win:
                states[neib].visits+=1
                if states[neib].visits == states[neib].edgesFrom:
                    states[neib].win = False
                    DFS(neib)
            else:
                states[neib].win = True
                DFS(neib)
def findCycle(graph: list):
    
    def DFS(start: int,graph: list,colors: list,previous: list):
        colors[start] = 1
        for vert in graph[start]:
            if colors[vert]==0:
                previous[vert] = start
                if DFS(vert,graph,colors,previous):
                    return True
            elif colors[vert]==1:
                return True
        colors[start] = 2
        return False
    previous = [0 for _ in range(len(graph))],
    colors = [None for _ in range(len(graph))]
    for i in range(len(graph)):
        if colors[i]!=2:
            if DFS(i,graph,colors,previous):
                return True
    return False
    



vertexQ,edgeQ,start = map(int,input().split())
invertedGraph = [[] for _ in range(vertexQ)]
states = [State() for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    states[vertex1].edgesFrom+=1
    invertedGraph[vertex2].append(vertex1)
leaves = []
for vertex,state in enumerate(states):
    if not state.edgesFrom:
        states[vertex].win = False
        leaves.append(vertex)
for leaf in leaves:
    DFS(leaf)
if not states[start].definedState() or findCycle(invertedGraph):
    print("Draw")
    exit()
elif states[start].win:
    print("Win")
    exit()
print("Lose")