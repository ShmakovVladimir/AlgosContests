insert,delete,replace = map(int,input().split())
s1,s2 = str(input()),str(input())
Dist = [[(i*delete+j*insert)*int(i*j==0) for j in range(len(s2)+1)] for i in range(len(s1)+1)]
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            Dist[i][j] =Dist[i-1][j-1]
        else:
            Dist[i][j] = min(Dist[i-1][j]+delete,Dist[i][j-1]+insert,Dist[i-1][j-1]+replace)
print(Dist[-1][-1])