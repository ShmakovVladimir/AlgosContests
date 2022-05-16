
class vertex:
    def __init__(self,value = None,left = None,right = None,height = 0):
        self.value = value
        self.left = left
        self.right = right
        self.height = 0
class Tree:
    def __init__(self,startValues = None):
        self.root = None
        if startValues is not None:
            for value in startValues:
                self.append(value)
    def append(self,value: int):
        if self.root is None:
            self.root = vertex(value)
            return
        vert = self.root
        while vert is not None:
            prevVert = vert
            if value>vert.value:
                vert = vert.right
            elif value<vert.value:
                vert = vert.right
            else:
                return 
        if prevVert.value < value:
            prevVert.right = vertex(value)
            return
        prevVert.left = vertex(value)
        
            

