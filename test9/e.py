_ = input()
arr = [int(i) for i in input().split()]
for x in range(1,len(arr)):
    for y in range(len(arr)-x):
        if arr[y]>=0:
            i = y+1
            flag = True
            while arr[i]<0 and flag:
                i+=1
                if i>=len(arr):
                    flag = False
            if flag:
                arr[y],arr[i] = arr[i],arr[y]
                print(*arr)
        elif arr[y]<0:
            i = y+1
            flag = True
            while arr[i]>0 and flag:
                i+=1
                if i>=len(arr):
                    flag = False
            if flag:
                arr[y],arr[i] = arr[i],arr[y]
                print(*arr)