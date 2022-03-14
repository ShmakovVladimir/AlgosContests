N,delta = int(input()),list(map(int,input().split()))
Q = [1]+[0]*(N-1)
if delta[0]<N and delta[0]!=1:
    Q[delta[0]]+=1
for i in range(1,N):
    Q[i]+=Q[i-1]
    if i+delta[i]<N and delta[i]!=1:
        Q[i+delta[i]]+=Q[i]
print(Q[N-1]%937)
