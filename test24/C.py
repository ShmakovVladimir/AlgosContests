dots,symmetryDot,ans = list(map(int,input().split())),list(map(int,input().split())),[] 
for i in range(len(dots)):
    ans.append(symmetryDot[i%2]+(int(dots[i]<symmetryDot[i%2])*2-1)*abs(symmetryDot[i%2]-dots[i]))
print(*ans)



