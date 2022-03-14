class dataAndTime:
    def __init__(self,date: str) -> None:
        self.date,self.month,self.year,self.time= date.split()
        self.data = date
        self.date,self.year,self.time = int(self.date),int(self.year),int(self.time.split(':')[0])*60+int(self.time.split(':')[1])
        self.months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    def comp(self,another) -> bool:
        if self.year>another.year:  return True
        if self.year<another.year: return False
        if self.months.index(self.month)>self.months.index(another.month):  return True
        if self.months.index(self.month)<self.months.index(another.month):  return False
        if self.date>another.date:  return True
        if self.date<another.date:  return False
        if self.time>=another.time: return True
        else:   return False
data = []
for _ in range(int(input())):   data.append(dataAndTime(str(input())))
for x in range(1,len(data)):
    element = data[x]
    x-=1
    while x>=0 and data[x].comp(element):
        data[x],data[x+1] = data[x+1],data[x]
        x-=1
for i in data:  print(i.data)