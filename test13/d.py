def lcs(s1: list,s2: list):
    maxL = [[0]*len(s2) for _ in range(len(s1))]
    i = j = 0
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            if s1[i-1]==s2[j-1]:    maxL[i][j] = maxL[i-1][j-1]+1
            else:   maxL[i][j] = max(maxL[i-1][j],maxL[i][j-1])
    subSeq = []
    while i>0 and j>0:
        if s1[i-1] == s2[j-1]:
            subSeq.append(s1[i-1])
            i-=1
            j-=1
        else:
            i-=int(maxL[i-1][j]>=maxL[i][j-1])
            j-=int(maxL[i-1][j]<maxL[i][j-1])
    if s1[-1]==s2[-1]:  subSeq = [s1[-1]]+subSeq
    return subSeq[::-1]