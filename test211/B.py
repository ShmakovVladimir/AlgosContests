_,_ = map(int,input().split())
stones = list(map(int,input().split()))
xorSum = stones[0]
for i in range(1,len(stones)):
    xorSum^=stones[i]
if xorSum == 0:
    print("YES")
    exit()
print("NO")