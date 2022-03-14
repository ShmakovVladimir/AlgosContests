
students = [[] for _ in range(int(input()))]
results = str(input())
while results!='#':
    student_id,value = int(results.split()[0]),int(results.split()[1])
    students[student_id].append(value)
    results = str(input())
for i in students:
    i.sort(reverse=True)
students.sort(key=lambda x:sum(x),reverse=True)
answer = ''
for i in students:
    for x in i:
        answer+=str(x)+' '
print(answer)