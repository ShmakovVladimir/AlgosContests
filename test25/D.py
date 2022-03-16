veretexQ,edgeQ = map(int,input().split())
graphMatrix= [[False]*veretexQ for _ in range(veretexQ)]
for i in range(edgeQ):
    j,k = map(int,input().split())
    graphMatrix[j][k] = True
for j in range(veretexQ):
    for k in range(j+1,veretexQ):
        if (not graphMatrix[j][k] )and (not graphMatrix[k][j]):
            print("NO")
            exit()
print("YES")
