letters = ['a','b','c','d','e','f','g','h']
N,Q = int(input()),[[0]*8 for _ in range(8)]
playGround = [[False]*8 for _ in range(8)]
for _ in range(N):
    coordinate = input()
    x,y = letters.index(coordinate[0]),int(coordinate[1])-1
    playGround[x][y] = True
coordinate = input()
x,y = letters.index(coordinate[0]),int(coordinate[1])-1
Q[x][y] = 1 
for y in range(1,8):
    for x in range(8):
        if playGround[x][y]:
            if x>0: Q[x][y]+=Q[x-1][y-1]
            if x<7: Q[x][y]+=Q[x+1][y-1]
        else:   Q[x][y]+=Q[x][y-1]
print(sum([Q[i][7] for i in range(8)]))
