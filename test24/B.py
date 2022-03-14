groundhogX,groundhogY = map(int,input().split())
dogX,dogY = map(int,input().split())
holes = []
for i in range(int(input())):
    x,y = map(int,input().split())
    holes.append({'x': x,'y': y})
for i in range(len(holes)):
    groundhogDist = ((holes[i]['x']-groundhogX)**2+(holes[i]['y']-groundhogY)**2)**.5
    dogDist = ((holes[i]['x']-dogX)**2+(holes[i]['y']-dogY)**2)**.5
    if groundhogDist<=dogDist/2:
        print(i+1)
        exit()
print("-1")