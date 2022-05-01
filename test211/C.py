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
if not states[start].definedState():
    print("Draw")
    exit()
elif states[start].win:
    print("Win")
    exit()
print("Lose")