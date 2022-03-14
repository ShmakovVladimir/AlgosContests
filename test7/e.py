arr = [int(i) for i in str(input()).split()]
rank, allZeros = 0,False
while not allZeros:
    allZeros,buffer = True,[[] for _ in range(10)]
    for i in arr:
        buffer[(i//(10**rank))%10].append(i)
        if (i//(10**rank))%10 != 0:    allZeros = False
    if allZeros:    break
    arr.clear()
    for x in range(10):
        for y in range(len(buffer[x])):
            arr.append(buffer[x][y])
    rank+=1
    print(*arr)
