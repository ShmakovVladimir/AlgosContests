N = int(input())
cell_color = list(map(int,input().split()))
jar_color = list(map(int,input().split()))
Q = [1,int(jar_color[0]==cell_color[1] or cell_color[0]==cell_color[1])]+[0]*(N-2)
for i in range(2,N):
    #если кузнечик может попасть из предыдущей клетки
    if cell_color[i]==cell_color[i-1] or jar_color[i-1]==cell_color[i]:
        Q[i]+=Q[i-1]
    if cell_color[i]==cell_color[i-2] or jar_color[i-2]==cell_color[i]:
        Q[i]+=Q[i-2]
print(Q[N-1]%947)
    