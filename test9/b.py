def split_barrier(A: list, barrier):
    left,right,middle = [],[],[]
    for i in A:
        if i<barrier:   left.append(i)
        elif i>barrier:    right.append(i)
        else:   middle.append(i)
    A.clear()
    for i in left: A.append(i)
    for i in middle:    A.append(i)
    for i in right:    A.append(i) 