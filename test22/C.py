class Value:
	def __init__(self,h,key,value):
		self.h,self.key,self.value = h,key,value
	def print(self):
		print(str(self.h)+' '+str(self.key)+' '+str(self.value))
def hash_function(s) -> int:
		h,base,module = 0,91,100
		for i in s:
			h*=base
			h+=ord(i)
			h%=module
		return h
class hash_table:
	def __init__(self,size = 10):
		self.size = size
		self.table = [[] for _ in range(self.size)]
	def insert(self,data):
		key,s = data.split()
		h = hash_function(key)
		element = h%self.size
		if key in [i.key for i in self.table[element]]:
			num = [i.key for i in self.table[element]].index(key)
			self.table[element][num] = Value(h,key,s)
		else:
			self.table[element].append(Value(h,key,s))
	def print_table(self):
		for line,i in enumerate(self.table):
			if i!=[]:
				print(line)
				for j in i:
					j.print()





#Test data
table = hash_table()
N = int(input())
for _ in range(N):
	table.insert(input())
table.print_table()