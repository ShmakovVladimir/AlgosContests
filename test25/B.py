graphMatrix = []
for i in range(int(input())):
    graphMatrix.append(list(map(int,input().split())))
for i in range(len(graphMatrix)):
    for j in range(len(graphMatrix)):
        if bool(graphMatrix[i][j]):
            print(str(i)+' '+str(j)+' '+str(graphMatrix[i][j]))
