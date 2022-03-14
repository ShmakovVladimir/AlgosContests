arr = [int(i) for i in str(input()).split()]
result,isZero,notZero,counter= [],[],[],0
for i in arr:
    if i == 0:
        isZero.append(True)
    else:
        notZero.append(i)
        isZero.append(False)
notZero.sort()
for i in isZero:
    if i:   result.append(0)
    else:   
        result.append(notZero[counter])
        counter+=1
print(*result)