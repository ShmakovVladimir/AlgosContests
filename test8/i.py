PLUS,MINUS = 1,2
MULT,DIV = 3,4
RIGHT,LEFT = 5,6
EOE,UNAR_MINUS = 7,8
NUMBER,EXP = 9,10



class token:
    def __init__(self,type,value = float("NAN")) -> None:
        self.type,self.value = type,value
def eqToken(eq: str):
    pos,a = 0,[]
    while pos<len(eq):
        char = eq[pos]
        if char == '+':
            a.append(token(PLUS))
        elif char == '-':
            a.append(token(MINUS))
        elif char == '(':
            a.append(token(LEFT))
        elif char == ')':
            a.append(token(RIGHT))
        elif char == '*':
            a.append(token(MULT))
        elif char == '/':
            a.append(token(DIV))
        elif char == '^':
            a.append(token(EXP))
        elif char>='0' and char<='9':
            num = 0
            while pos<len(eq) and eq[pos]>='0' and eq[pos]<='9':
                num*=10
                num+=int(eq[pos])
                pos+=1
            a.append(token(NUMBER,num))
        pos+=1
        a.append(token(EOE))
        return a


        
            