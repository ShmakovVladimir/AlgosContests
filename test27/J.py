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
        return neib
    def __eq__(self,other):
        return (self.x==other.x and self.y == other.y)


gridHeight,gridWidth = map(int,input().split())
grid = []
for _ in range(gridHeight):
    grid.append([int(i) for i in input().split()])
dist = [[0 for _ in range(gridWidth)] for _ in range(gridHeight)]
start = queue.Queue(0)
for x in range(gridWidth):
    for y in range(gridHeight):
        if grid[y][x]:
            start.put(Point(x,y))
while not start.empty():
    cell = start.get()
    for neib in cell.neibors():
        if not grid[neib.y][neib.x]:
            grid[neib.y][neib.x] = 1
            start.put(neib)
            dist[neib.y][neib.x] = dist[cell.y][cell.x]+1
for i in range(len(dist)):
    print(*dist[i])

