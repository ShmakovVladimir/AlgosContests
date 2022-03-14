def lis(s: list):
    maxL = [0]*len(s)
    for x in range((len(s))):
        maxL[x] = 1+max([0]+[maxL[i] if s[i] < s[x] else 0 for i in range(x)])
    mInd = maxL.index(max(maxL))
    sub = [s[mInd]]
    while mInd>0 and maxL[mInd]>1:
        k= mInd
        while k>=-1 and maxL[mInd]!=maxL[k]+1:    k-=1
        if k!=-1:   sub.append(s[k])
        mInd = k
    return sub[::-1]

        
