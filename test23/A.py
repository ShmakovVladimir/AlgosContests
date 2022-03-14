france = {int(i) for i in input().split()}
swim = {int(i) for i in input().split()}
piano = {int(i) for i in input().split()}
result = (piano&swim) - france
ans = sorted([i for i in result])
print(*ans)