
def sgn(value: float) ->int:
    if value == 0:
        return 0
    return int(value/abs(value))
def check(dot: list,vertex1: list,vertex2: list,checkVertex: list)->bool:
    A,B = vertex1[1]-vertex2[1],vertex2[0]-vertex1[0]
    C = -(A*vertex1[0]+B*vertex1[1])
    return sgn(A*dot[0]+B*dot[1]+C) == sgn(A*checkVertex[0]+B*checkVertex[1]+C) or sgn(A*dot[0]+B*dot[1]+C) == 0
N,vertexCrr = int(input()),[]
for _ in range(N):
    vertexCrr.append(list(map(float,input().split())))
dotCrr = list(map(float,input().split()))
for i in range(N-2):
    if not check(dotCrr,vertexCrr[i],vertexCrr[i+1],vertexCrr[i+2]):
        print("NO")
        exit()
if not check(dotCrr,vertexCrr[-2],vertexCrr[-1],vertexCrr[0]):
        print("NO")
        exit()
if not check(dotCrr,vertexCrr[-1],vertexCrr[0],vertexCrr[len(vertexCrr)//2]):
        print("NO")
        exit()
print("YES")


