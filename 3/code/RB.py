from Node import Node


class RedBlackTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        currentNode = self.root
        while currentNode is not None:
            if currentNode.value == value:
                return currentNode
            elif currentNode.value < value:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
            return None

    def insert(self, value):
        newNode = Node(value)
        if (self.root is None):
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if currentNode.value > value:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        newNode.parent = currentNode
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        newNode.parent = currentNode
                        break
                    else:
                        currentNode = currentNode.right
        self.insertFix(newNode)

    def insertFix(self, newNode):
        while newNode.parent and newNode.parent.color == 'red':
            if newNode.parent == newNode.getGrandParent().left:
                uncle = newNode.uncle()
                if uncle and uncle.color == 'red':
                    newNode.parent.color = 'black'
                    uncle.color = 'black'
                    newNode.getGrandParent().color = 'red'
                    newNode = newNode.getGrandParent()
                else:
                    if newNode == newNode.parent.right:
                        newNode = newNode.parent
                        self.rotateLeft(newNode)
                    newNode.parent.color = 'black'
                    newNode.getGrandParent().color = 'red'
                    self.rotateRight(newNode.getGrandParent())
            else:
                uncle = newNode.getUncle()
                if uncle and uncle.color == 'red':
                    newNode.parent.color = 'black'
                    uncle.color = 'black'
                    newNode.getGrandParent().color = 'red'
                    newNode = newNode.getGrandParent()
                else:
                    if newNode == newNode.parent.left:
                        newNode = newNode.parent
                        self.rotateRight(newNode)
                    newNode.parent.color = 'black'
                    newNode.getGrandParent().color = 'red'
                    self.rotateLeft(newNode.getGrandParent())
        self.root.color = 'black'

    def GetHeight(self, node):
        if node is None:
            return 0
        left_height = self.GetHeight(node.left)
        right_height = self.GetHeight(node.right)
        return 1 + max(left_height, right_height)

    def BlackHeight(self):
        node = self.root
        counter = 0
        while (node is not None):
            if node.color == 'black':
                counter += 1
            node = node.left
        return counter

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


list = [1, 2, 3]
tree = RedBlackTree()
for i in list:
    tree.insert(i)
print(tree.GetHeight(tree.root))
print(tree.BlackHeight())