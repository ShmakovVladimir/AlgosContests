def A(m,n):
    if m == 0:
        return n+1
    if m>0 and n==0:
        return A(m-1,1)
    return A(m-1,A(m,n-1))
m,n = int(input()),int(input())
print(A(m,n))