import math
def buildsqrtComp(arr: list)->list:
    sqrtCmp = [float("-inf")]*int(len(arr)**.5+0.5001)
    for i in range(len(arr)):
        sqrtCmp[math.floor(i/len(sqrtCmp))] = int(sqrtCmp[math.floor(i/len(sqrtCmp))] < arr[i])*arr[i] + int(sqrtCmp[math.floor(i/len(sqrtCmp))] >= arr[i])*sqrtCmp[math.floor(i/len(sqrtCmp))]
    return sqrtCmp
def rmq(left: int,right: int,sqrtCmp: list)->int:
    l = math.floor(left/len(sqrtCmp))
    r = math.floor(right/len(sqrtCmp))
    ans = float("-inf")
    for i in range(l,r):
        if sqrtCmp[i]>ans:
            ans = sqrtCmp[i]

    
_,arr = input(),[int(i) for i in input().split()]
sqrtCmp = buildsqrtComp(arr)
for i in range(int(input())):
    left,rigth = map(int,input().split())
    print(rmq(left,rigth,sqrtCmp))
    