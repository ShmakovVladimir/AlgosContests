def det(n,matrix):
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
    d = 0
    for i in range(n):
        d+=((-1)**i)*matrix[i][0]*det(n-1,[matrix[j][1:n] for j in (list(range(i))+list(range(i+1,n)))])
    return d
n,matrix = int(input()),[]
for i in range(n):
    matrix.append([int(k) for k in str(input()).split()])
print(det(n,matrix))