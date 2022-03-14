N,M = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(str(len(set(a)))+" "+str(len(set(b)))+" "+str(len(set(a+b))))
