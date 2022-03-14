
N = int(input())
Q = [1,0,3]+[0]*(N-3)
for i in range(4,N,2):
    Q[i] = 2*(Q[i-2])
    for j in range(0,i,2):
        Q[i]+=Q[j]
print(Q[N-1])

    