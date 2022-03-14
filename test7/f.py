def bubble_sort2d(matrix, N, M):
    flag = False
    while not flag:
        flag = True
        for x in range(N):
            for y in range(M):
                if x==N-1 and y==M-1:
                    break
                ind1,ind2 = x,y+1
                if ind2>=M:
                    ind1+=1
                    ind2 = 0
                if matrix[x][y] > matrix[ind1][ind2]:
                    flag=False
                    for i in range(N):  print(*matrix[i])
                    print()
                    matrix[x][y], matrix[ind1][ind2] = matrix[ind1][ind2], matrix[x][y]
    for i in range(N):  print(*matrix[i])
    print()           