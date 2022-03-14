aX,aY,aR = map(int,input().split())
bX,bY,bR = map(int,input().split())
centerDist = ((aX-bX)**2+(aY-bY)**2)**.5
eps = 10**(-5)
if centerDist-eps<=(aR+bR) and centerDist+aR>=bR-eps and centerDist+bR>=aR-eps:
    print("YES")
    exit()
print("NO")