class state:
    def __init__(self,win = None,counter = 0):
        self.win = win
        self.counter = counter
    def filled(self)->bool:
        return not self.win is None
def play(start: int,graph: list,states: list,edgesFrom: list):
    for neib in graph[start]:
        if not states[neib].filled():
            if not states[start].win:
                states[neib].win = True
                play(neib,graph,states,edgesFrom)
            else:
                states[neib].counter+=1
                if states[neib].counter == edgesFrom[neib]:
                    states[neib].win = False
                    play(neib,graph,states,edgesFrom)


vertexQ,edgeQ,start = map(int,input().split())
invertedGraph = [[] for _ in range(vertexQ)]
edgesFrom = [0 for _ in range(vertexQ)]
withNoOuts = [True for _ in range(vertexQ)]
states = [state() for _ in range(vertexQ)]
for _ in range(edgeQ):
    vertex1,vertex2 = map(int,input().split())
    invertedGraph[vertex2].append(vertex1)
    edgesFrom[vertex1]+=1
for vertex,i in enumerate(withNoOuts):
    if i:
        states[vertex].win = False
        play(vertex,invertedGraph,states,edgesFrom)
if not states[start].filled():
    print("Draw")
    exit()
if states[start].win:
    print("Win")
    exit()
print("Lose")



        
        



