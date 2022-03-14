def BinaryFind(where: list,what, left: int, right:int):
    if where[left] == what:
        return left+1
    if where[right-1] == what:
        return right
    if right-left<=1:
        return -1
    if where[(left+right)//2] < what: 
        return BinaryFind(where,what,(right+left)//2,right)
    elif where[(left+right)//2] > what: 
        return BinaryFind(where,what,left,(right+left)//2)
    return 1+((left+right)//2)
arr,N = list(map(int,input().split())),int(input())
print(BinaryFind(arr,N,0,len(arr)))