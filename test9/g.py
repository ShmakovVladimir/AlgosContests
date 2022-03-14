def hoar_sort(A, depth=1, part='left'):
    if len(A)<=1:
        return
    left,right,middle = [],[],[]
    barrier = A[len(A)//2]
    for i in A:
        if i<barrier:   left.append(i)
        elif i>barrier:    right.append(i)
        else:   middle.append(i)
    #Рекурсивно сортируем "левую" и "правую" часть
    hoar_sort(left,depth+1,'left')
    hoar_sort(right,depth+1,'right')
    A.clear()
    for i in left: A.append(i)
    for i in middle:    A.append(i)
    for i in right:    A.append(i)
def deleteSame(arr):
    alpha,result = [True for _ in range(len(arr))],[]
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:  alpha[i]=False
    for i in range(len(alpha)):
        if alpha[i]:    result.append(arr[i])
    return result

_ = input()
arr1,arr2 = [int(i) for i in input().split()],[int(j) for j in input().split()]
hoar_sort(arr1)
arr1 = deleteSame(arr1)
hoar_sort(arr2)
arr2 = deleteSame(arr2)
if arr1==arr2:
    print("Yes")
else:
    print("No")