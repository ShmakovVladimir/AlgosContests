N,creep = int(input()),list(map(int,input().split()))
dirtiness = [creep[0],creep[1]]+[0]*(N-2)
way = [[] for _ in range(N)]
way[0],way[1] = [0],[1]
for i in range(2,N):
    dirtiness[i] = min(dirtiness[i-1],dirtiness[i-2])+creep[i]
    if dirtiness[i-1]<dirtiness[i-2]:   way[i]= way[i-1]+[i]
    else:   way[i] = way[i-2]+[i]
print(dirtiness[N-1])
print(*way[N-1])