
def chekSize(a,b,N,size):
    if a==0 and b==0:
        return True
    if a == 0 and size<=b:  
        return True
    if b == 0 and size<=a:  
        return True
    elif N//(size//b) + 1<= size//a:
        return True
    return False
def binarySearch(a,b,N):
    left,right = min(a,b),max(a*N,b*N)
    while right-left>1:
        size = (left+right)//2
        if chekSize(a,b,N,size):
            right = size
        else:   left = size
    return right
a,b,N = map(int,input().split())
print(binarySearch(a,b,N))