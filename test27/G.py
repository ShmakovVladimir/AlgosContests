import queue

class Point:
    def __init__(self,x,y) -> None:
        self.x,self.y = x,y
    def neibors(self) -> list:
        global gridHeight,gridWidth
        neib = []
        if self.x+1<gridWidth:
            neib.append(Point(self.x+1,self.y))
        if self.x-1>=0:
            neib.append(Point(self.x-1,self.y))
        if self.y-1>=0:
            neib.append(Point(self.x,self.y-1))
        if self.y+1<gridHeight:
            neib.append(Point(self.x,self.y+1))
        if self.x+1<gridWidth and self.y-1>=0:
            neib.append(Point(self.x+1,self.y-1))
        if self.x+1<gridWidth and self.y+1<gridHeight:
            neib.append(Point(self.x+1,self.y+1))
        if self.x-1>=0 and self.y+1<gridHeight:
            neib.append(Point(self.x-1,self.y+1))
        if self.x-1>=0 and self.y-1>=0:
            neib.append(Point(self.x-1,self.y-1))
        return neib
    def __eq__(self,other):
        return (self.x==other.x and self.y == other.y)
gridHeight,gridWidth = map(int,input().split())
startY,startX = map(int,input().split())
endY,endX = map(int,input().split())
start,end = Point(startX,startY),Point(endY,endX)

grid = [[None for _ in range(gridHeight)] for _ in range(gridWidth)]
for y in range(gridHeight):
    string = input()
    for x,symb in enumerate(string):
        grid[x][y] = (symb == ' ')

steck,dist = queue.Queue(0),[[0 for _ in range(gridHeight)] for _ in range(gridWidth)]
steck.put(start)
grid[start.x][start.y] = False
alpha = True
while alpha and (not steck.empty()):
    cell = steck.get()
    for neib in cell.neibors():
        if grid[neib.x][neib.y]:
            grid[neib.x][neib.y] = False
            steck.put(neib)
            dist[neib.x][neib.y] = dist[cell.x][cell.y]+1
            if neib == end:
                alpha = False
if not alpha:
    print(dist[end.x][end.y])
    exit()
print("INF")