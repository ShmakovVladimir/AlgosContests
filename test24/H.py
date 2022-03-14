from math import ceil
from math import log2
class Tree:
    def __init__(self,arr: list) -> None:
        self.buildTree(arr)
    def buildTree(self,arr: list):
        nuArr = arr+[float("-inf")]*(2**ceil(log2(len(arr)))-len(arr))
        self.tree = [0]*(2*len(nuArr)-1)
        for i in range(len(nuArr)):
            self.tree[len(nuArr)+i-1] = [nuArr[i],i,i]
        for i in range(len(nuArr)-2,-1,-1):
            self.tree[i] = [max(self.tree[2*i+1][0],self.tree[2*i+2][0]),self.tree[2*i+1][1],self.tree[2*i+2][2]]
    def inRange(self,index: int,left: int,right: int)->bool:
        if self.tree[index][1]>=left and self.tree[index][2]<=right:
            return True
        return False
    def fullyNotInRange(self,index: int,left: int,right: int)->bool:
        if self.tree[index][2]<left or self.tree[index][1]>right:
            return True
        return False
    def RMQ(self,left: int,right: int,flag = 0)->float:
        if self.fullyNotInRange(flag,left,right):
            return float("-inf")
        if self.inRange(flag,left,right):
            return self.tree[flag][0]
        return max(self.RMQ(left,right,flag*2+1),self.RMQ(left,right,flag*2+2))
_,arr = input(),[int(i) for i in input().split()]
t = Tree(arr)
ans = []
for i in range(int(input())):
    left,right = map(int,input().split())
    ans.append((t.RMQ(left,right)))
print(*ans)
    