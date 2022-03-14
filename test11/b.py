N,y = int(input()),[]
for _ in range(N):  y.append(int(input()))
if N==1:    
    print(0)
    exit()
energy = [0,abs(y[1]-y[0])]+[0]*(N-2)
for i in range(2,N):
    energy[i] = min(energy[i-1]+abs(y[i-1]-y[i]),energy[i-2]+3*abs(y[i-2]-y[i]))
print(energy[N-1])
