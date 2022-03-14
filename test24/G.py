_,arr = input(),[int(i) for i in input().split()]
prefixSumArr,ans = [arr[0]]+[0]*(len(arr)-1),[]
for i in range(1,len(arr)):    
    prefixSumArr[i] = prefixSumArr[i-1]+arr[i]
for i in range(int(input())):
    left,right = map(int,input().split())
    ans.append(prefixSumArr[right]-prefixSumArr[left]+arr[left])
print(*ans)



