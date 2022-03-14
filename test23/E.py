def parents(tree: dict,name: str)->set:
    return tree.get(name,set())
def grandparents(tree: dict,name: str)->set:
    gp = set()
    for i in parents(tree,name):    
        gp|=tree.get(i,set())
    return gp
def children(tree: dict,name: str)->set:
    child = set()
    for i in tree.items():
        if name in i[1]:
            child|=set(i[0])
    return child
def grandchildren(tree: dict,name: str)->set:
    grandChild = set()
    for i in children(tree,name):
        grandChild|=children(tree,i)
    return grandChild
def siblings(tree: dict,name: str)->set:
    sub = set()
    for i in parents(tree,name):
        sub|=children(tree,i)
    sub-=set(name)
    return sub