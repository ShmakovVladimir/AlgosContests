a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())
delta = a1*b2-a2*b1
delta1 = -c1*b2+c2*b1
delta2 = -c2*a1+c1*a2
if delta == 0 and c1 == 0 and c2 == 0:
    print('0 0')
if delta == 0:
    print("NO")
    exit()
print(str(round(delta1/delta))+" "+str(round(delta2/delta)))


