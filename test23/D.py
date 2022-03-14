text,capitals= input(),{chr(i): 0 for i in range(65,91)}
for i in text:
    if i!=' ':
        capitals[i]+=1
for i in sorted(capitals.items()):
    if i[1] !=0:
        print(*i)


