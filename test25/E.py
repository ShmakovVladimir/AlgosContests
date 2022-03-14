graphMatrix,sources,stocks = [],[],[]
for i in range(int(input())):
    graphMatrix.append([int(i) for i in input().split()])
for j in range(len(graphMatrix)):
    if sum(graphMatrix[j])==0:
        stocks.append(j+1)
    sigma = 0
    for k in range(len(graphMatrix)):
        sigma+=graphMatrix[k][j]
    if sigma == 0:
        sources.append(j+1)
print(*sources)
print(*stocks)