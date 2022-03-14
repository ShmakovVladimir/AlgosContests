class card:
    def __init__(self,c: str):
        self.suit,self.value = c[0],int(c[1])
    def __eq__(self,other):
        if self.suit == other.suit and abs(self.value-other.value)<3:
            return True
        return False
    def __lt__(self,other):
        if self.suit == other.suit:
            return True
        return False
take,steck = 0,[]
alpha = input().split()
for i in alpha:
    steck.append(card(i))
    if len(steck)>=2 and steck[-1] == steck[-2]:
        take+=2
        steck.pop()
        steck.pop()
        if len(steck)>=2 and steck[-1]<steck[0]:
            steck.pop(0)
            steck.pop()
            take+=2
print(take)