x1,y1,x2,y2 = map(float,input().split())
x,y = map(float,input().split())
a1,b1 = y2-y1,x1-x2
c1 = -(a1*x1+b1*y1)
a2,b2 = x2-x1,y2-y1
c2 = -((a2*x+b2*y))
delta = a1*b2-a2*b1
delta1 = -c1*b2+c2*b1
delta2 = -c2*a1+c1*a2
if delta == 0 and c1 == 0 and c2 == 0:
    xSym = ySym = 0
else:
    xSym = delta1/delta
    ySym = delta2/delta
print(str(round(xSym+(int(x<xSym)*2-1)*abs(xSym-x),5))+" "+str(round(ySym+(int(y<ySym)*2-1)*abs(ySym-y),5)))

