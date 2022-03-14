def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
    if len(A)<=1:
        return
    left,right,middle = [],[],[]
    barrier = A[0]
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
    

    print('depth:', depth, 'part:', part, 'array after:', A)