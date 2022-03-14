graphMatrix = []
for i in range(int(input())):
    graphMatrix.append(list(map(bool,input().split())))
for i in range(len(graphMatrix)):
    if 
    for j in range(min(i,len(graphMatrix)-i)):
        if not graphMatrix[i][i+j]*graphMatrix[i][i-j]:
            print("NO")
            exit()
print("YES")