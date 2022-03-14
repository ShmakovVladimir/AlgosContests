def BinaryFind(where: list,what):
    left,right = 0,len(where)
    while right-left>1:
        if what<where[(left+right)//2]:  right = ((left+right)//2)
        elif what>where[(left+right)//2]:   left = ((left+right)//2)
        else:   return 1+(left+right)//2
    if where[left] == what:
        return left+1
    return -1
_,K,arr = input(),int(input()),[int(i) for i in str(input()).split()]
print(BinaryFind(arr,K))
