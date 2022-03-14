def is_possible(crr,K: int,min_dist):
    previousPosition,j = crr[0],1
    for i in range(1,len(crr)):
        if crr[i]-previousPosition >= min_dist:  
            j+=1 #ставим лошадь
            previousPosition = crr[i]
    if j>=K:    
        return True
    return False
def binSearch(crr,K):
    left,right = 0,crr[len(crr)-1]-crr[0]+2
    while right-left>1:
        if is_possible(crr,K,(left+right)//2):  left = (left+right)//2
        else:   right = (left+right)//2
    return left
    
_,K = map(int,input().split())
crr = [int(i) for i in input().split()]
print(binSearch(crr,K))