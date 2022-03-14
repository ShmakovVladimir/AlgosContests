def Calc(a: int,b: int,op:str)->int:
    if op == '/':
        return b/a
    return int(op=='*')*b*a+int(op=='+')*(b+a)+int(op=='-')*(b-a)
i,steck = input(),[]
while i!='=':
    if len(i)==1 and ord(i)>41 and ord(i)<48:
        steck.append(Calc(steck.pop(),steck.pop(),i))
    else:
        steck.append(int(i))
    i = input()
print(steck[0])