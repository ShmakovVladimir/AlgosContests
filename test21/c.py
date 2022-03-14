a = str(input())
counter = 0
ans = ''
for i in a:
     ans+=(str(counter)+'^01*'+i+' + ')
     counter+=1
print((ans)[3::])