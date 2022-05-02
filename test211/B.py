
def win(stones: list)->bool:
    ans = stones[0]
    for i in range(1,len(stones)):
        ans^=stones[i]
    return ans==0

heapQ,maxPick = map(int,input().split())
startState = list(map(int,input().split()))

for heapNum in range(len(startState)):
    newState = startState.copy()
    for _ in range(maxPick+1):
        if win(newState):
            print("YES")
            exit()
        newState[heapNum]-=1
print("NO")
