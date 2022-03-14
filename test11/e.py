N = int(input())
B = [1,2,4]+[0]*(N-3)
A = [1,2,3]+[0]*(N-3)
for i in range(3,N):
    B[i] = B[i-1]+A[i-1]
    A[i] = B[i-1]
    for j in range(1,i//2):
        A[i]+=(int((j+1)%2==0)*A[i-j])
print(A[N-1]+B[N-1])