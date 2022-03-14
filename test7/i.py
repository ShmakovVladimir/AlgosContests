def merge(L,R):
    result,l= [0]*(len(L)+len(R)),0
    if len(L)>len(R):
        L,R = R,L
    if len(L)==0:
        return R
    for r in range(len(R)):
        while l<len(L) and L[l]<R[r] :
            result[l+r] = L[l]
            l+=1
        result[l+r] = R[r]
    for i in range(l,len(L)):
        result[len(R)+i] = L[i]
    return result

        
    
