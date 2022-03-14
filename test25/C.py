graphMatrix,ans = [],0
for i in range(int(input())):
    graphMatrix.append(list(map(int,input().split())))
for i in range(len(graphMatrix)):
    for j in range(i+1,len(graphMatrix)):
        ans+=graphMatrix[i][j]
print(ans)
