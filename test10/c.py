def find_root(f, a, b, tol):
    middle = (a+b)/2
    while abs(f(middle))>tol:
        middle = (a+b)/2
        if f(middle)>0:    b=middle
        else:   a=middle
    return middle
def f(x):
    return x**3-125
print(find_root(f,0,100,0.0001))