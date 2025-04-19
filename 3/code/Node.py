class Node:
    def __init__(self,value,color="red"):
        self.value=value
        self.color=color
        self.parent=None
        self.left=None
        self.right=None

    def getGrandParent(self):
        if (self.parent is None):
            return None
        return self.parent.parent
    
    def getSibling(self):
        if (self.parent is None):
            return None
        if self==self.parent.left:
            return self.parent.right
        return self.parent.left
    
    def getUncle(self):
        if (self.parent is None):
            return None
        return self.parent.getSibling()
    
    