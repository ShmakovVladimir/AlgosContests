def is_add_35(n: int)->bool:
    if n<=0: 
        return False
    if n in [1,4,6]:
        return True
    return is_add_35(n-3) or is_add_35(n-5)