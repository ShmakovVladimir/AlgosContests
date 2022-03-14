graphMatrix = []
for i in range(int(input())):
    graphMatrix.append([int(i) for i in input().split()])
for j in range(len(graphMatrix)):
    for k in range(i,len(graphMatrix)):
        if not graphMatrix[j][k]==graphMatrix[k][j] and not bool(graphMatrix[j][j]):
            print("NO")
            exit()
print("YES")