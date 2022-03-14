base,module = map(int,input().split())
s,h = input(),0
for i in s:
    h*=base
    h+=ord(i)
    h%=module
print(h)
