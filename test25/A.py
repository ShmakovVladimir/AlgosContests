graphMatrix = []
for i in range(int(input())):
    graphMatrix.append(list(map(bool,input().split())))
for i in range(len(graphMatrix)):
    if graphMatrix[i][i]:
        print("NO")
        exit()
    for j in range(i,len(graphMatrix)):
        if graphMatrix[i][j]!=graphMatrix[j][i]:
            print("NO")
            exit()
print("YES")
