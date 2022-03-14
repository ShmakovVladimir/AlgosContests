N,M = int(input()),int(input())
prices = [[0]*N for _ in range(M)]
for y in range(N):
    for x in range(M):
        prices[x][y] = int(input())
spend,money = [[0]*N for _ in range(M)],int(input())
for x in range(M):
    for y in range(N):
        if x==0 and y!=0:    spend[x][y] = spend[x][y-1]+prices[x][y]
        elif x!=0 and y==0:    spend[x][y] = spend[x-1][y]+prices[x][y]
        else:   spend[x][y] = min(spend[x-1][y],spend[x][y-1])+prices[x][y]
if money-spend[M-1][N-1]<0:
    print("Impossible")
else:   print(money-spend[M-1][N-1])