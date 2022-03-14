def subArrays(arr: list,index,length = 1):
    if index == 1:
        print(arr[0])
    else:
        nuLength,nuIndex = length+1,index
        if index == length:
            nuLength,nuIndex = 1,index-1
        subArrays(arr,nuIndex,nuLength)
        print(*arr[index-length:index])
a = str(input()).split()
subArrays(a,len(a))
