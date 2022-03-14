crr = list(map(int,input().split()))
crr.sort()
if len(crr)==2:
    print(crr[1]-crr[0])
    exit()
nCon = [0,float('+inf')]+[0]*(len(crr)-2)
wCon = [0,crr[1]-crr[0]]+[0]*(len(crr)-2)
for i in range(2,len(crr)-1):
    nCon[i] = wCon[i-1]+crr[i+1]-crr[i]
    wCon[i] = min(wCon[i-1]+crr[i]-crr[i-1],nCon[i-1])
print(min(wCon[len(crr)-2]+crr[len(crr)-1]-crr[len(crr)-2],nCon[len(crr)-2]))