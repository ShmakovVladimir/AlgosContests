def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A) 
    if len(A)<=1:   return
    L,R = A[:len(A)//2],A[len(A)//2:]
    merge_sort(L,depth+1)
    merge_sort(R,depth+1,'right')
    result,l= [0]*(len(L)+len(R)),0 
    if len(L)>len(R): 
        L,R = R,L 
    for r in range(len(R)): 
        while l<len(L) and L[l]<R[r] : 
            result[l+r] = L[l] 
            l+=1 
        result[l+r] = R[r] 
    for i in range(l,len(L)): 
        result[len(R)+i] = L[i] 
    A.clear()
    for i in result:    A.append(i)
    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)  