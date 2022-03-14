size = 10
def hash_function(s) -> int:
		h,base,module = 0,91,100
		for i in s:
			h*=base
			h+=ord(i)
			h%=module
		return h
def search(table,key):
	element = hash_function(key)%10
	keys =  [i[1] for i in table[element]]
	if key in keys:
		ind = keys.index(key)
		return table[element][ind][2]
	return 'KeyError'