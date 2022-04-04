import queue

def getPositionByCellName(cellName: str)->tuple:
    return ord(cellName[0])-97,int(cellName[1])-1

def getSteps(cellX: int,cellY: int)->list:
    steps = []
    if cellX+2<8 and cellY+1<8:
        steps.append((cellX+2,cellY+1))
    if cellX+2<8 and cellY-1>=0:
        steps.append((cellX+2,cellY-1))
    if cellX-2>=0 and cellY+1<8:
        steps.append((cellX-2,cellY+1))
    if cellX-2>=0 and cellY-1>=0:
        steps.append((cellX-2,cellY-1))
    if cellX-1>=0 and cellY+2<8:
        steps.append((cellX-1,cellY+2))
    if cellX-1>=0 and cellY-2>=0:
        steps.append((cellX-1,cellY-2))
    if cellX+1<8 and cellY-2>=0:
        steps.append((cellX+1,cellY-2))
    if cellX+1<8 and cellY+2<8:
        steps.append((cellX+1,cellY+2))
    return steps
    

def BFS(start: str):
    startPosX,startPosY = getPositionByCellName(start)
    grid = [[True for _ in range(8)] for _ in range(8)]
    steck,dist = queue.Queue(0),[[0 for _ in range(8)] for _ in range(8)]
    steck.put((startPosX,startPosY))
    grid[startPosX][startPosY] = False
    while not steck.empty():
        cellX,cellY = steck.get()
        for stepX,stepY in getSteps(cellX,cellY):
            if grid[stepX][stepY]:
                grid[stepX][stepY] = False
                steck.put((stepX,stepY))
                dist[stepX][stepY] = dist[cellX][cellY]+1
    return dist

start1,start2 = input().split()
ans = float("inf")
distances1,distances2 = BFS(start1),BFS(start2)
for x in range(8):
    for y in range(8):
        if distances1[x][y] == distances2[x][y] and distances2[x][y]<ans:
            ans = distances2[x][y]
if ans != float("inf"):
    print(ans)
    exit()
print(-1)