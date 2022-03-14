N = int(input())
alpha = [0,0]+[0]*(N)
for i in range(2,N+2):
    if i%3 == 0 and i%2 == 0:
        alpha[i] = 1+min(alpha[i//3],alpha[i//2],alpha[i-1])
    elif i%3 == 0:
        alpha[i] = 1+min(alpha[i//3],alpha[i-1])
    elif i%2==0:
        alpha[i] = 1+min(alpha[i//2],alpha[i-1])
    else:   alpha[i] = 1+alpha[i-1]
print(alpha[N])