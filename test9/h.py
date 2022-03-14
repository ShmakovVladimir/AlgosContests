def merge(L,R): 
    result,l= [0]*(len(L)+len(R)),0 
    if len(L)>len(R): 
        L,R = R,L 
    if len(L)==0: 
        return R 
    for r in range(len(R)): 
        while l<len(L) and L[l]>R[r] : 
            result[l+r] = L[l] 
            l+=1 
        result[l+r] = R[r] 
    for i in range(l,len(L)): 
        result[len(R)+i] = L[i] 
    return result
class proger:
    def __init__(self,total: str,name: str):
        self.total,self.name,self.totalStr = float(total),name,total
    def __it__(self,other)-> bool:
        if abs(self.total - other.total)<float('1e-5'):
            return self.name>other.name
        return self.total<other.total
    def __gt__(self,other)->bool:
        if abs(self.total - other.total)<float('1e-5'):
            return self.name<other.name
        return self.total>other.total
    def print(self):
        print(self.totalStr+' '+self.name)
numberOfRooms = int(input())
results,total = [[] for _ in range(numberOfRooms)],0
for room in range(numberOfRooms):
    numberOfPersons = int(input())
    total+=numberOfPersons
    for _ in range(numberOfPersons):
        s = input().split()
        results[room].append(proger(s[0],s[1]))
for room in range(len(results)-1):
    results[room+1] = merge(results[room],results[room+1])
print(total)
for i in results[len(results)-1]:
    i.print()
    


    




