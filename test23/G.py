data, stack = [i for i in input().split()],[]
for i in data:
	if i == '#' and stack !=[]:
		while len(stack)>1:
			stack[0]+=stack.pop()
	elif i == '#':
		print('0.0')
		exit()
	elif i == '%' and len(stack)>=2:
		num, procents = stack.pop(),stack.pop()
		stack.append(num*procents/100)
	elif i =='%':
		print('0.0')
		exit()
	else:
		stack.append(float(i))
print(stack[-1])