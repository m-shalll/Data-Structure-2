from Node import Node
class RedBlackTree:
    def __init__(self):
        self.root=None

    def search(self,value):
        currentNode=self.root
        while currentNode is not None:
            if currentNode.value==value:
                return currentNode
            elif currentNode.value<value:
                currentNode=currentNode.right
            else:
                currentNode=currentNode.left
            return None
    
    def insert(self,value):
        newNode=Node(value)
        if(self.root is None):
            self.root=newNode
        else:
            currentNode=self.root
            while True:
                if currentNode.value>value:
                    if currentNode.left is None:
                        currentNode.left=newNode
                        newNode.parent=currentNode
                        break
                    else:
                        currentNode=currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right=newNode
                        newNode.parent=currentNode
                        break
                    else:
                        currentNode=currentNode.right
        self.insertFix(newNode)

    def insertFix(self, newNode):
        while newNode.parent and newNode.parent.color == 'red':
            if newNode.parent == newNode.grandparent().left:
                uncle = newNode.uncle()
                if uncle and uncle.color == 'red':
                    newNode.parent.color = 'black'
                    uncle.color = 'black'
                    newNode.grandparent().color = 'red'
                    newNode = newNode.grandparent()
                else:
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.rotateLeft(newNode)
                    newNode.parent.color = 'black'
                    newNode.grandparent().color = 'red'
                    self.rotateRight(newNode.grandparent())
            else:
                uncle = newNode.uncle()
                if uncle and uncle.color == 'red':
                    newNode.parent.color = 'black'
                    uncle.color = 'black'
                    newNode.grandparent().color = 'red'
                    newNode = newNode.grandparent()
                else:
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rotateRight(newNode)
                    newNode.parent.color = 'black'
                    newNode.grandparent().color = 'red'
                    self.rotateLeft(newNode.grandparent())
        self.root.color = 'black'

    def rotateLeft(self, node):
        rightChild = node.right
        node.right = rightChild.left
        if rightChild.left is not None:
            rightChild.left.parent = node
        rightChild.parent = node.parent
        if node.parent is None:
            self.root = rightChild
        elif node == node.parent.left:
            node.parent.left = rightChild
        else:
            node.parent.right = rightChild
        rightChild.left = node
        node.parent = rightChild

    def rotateRight(self, node):
        leftChild = node.left
        node.left = leftChild.right
        if leftChild.right is not None:
            leftChild.right.parent = node

        leftChild.parent = node.parent
        if node.parent is None:
            self.root = leftChild
        elif node == node.parent.right:
            node.parent.right = leftChild
        else:
            node.parent.left = leftChild
        leftChild.right = node
        node.parent = leftChild