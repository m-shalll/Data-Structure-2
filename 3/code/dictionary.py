from RB import RedBlackTree
def loadDictionary(filename,tree):
    with open(filename,"r") as file:
        for line in file:
            tree.insert(line.strip())

def insertWord(word,tree):
    if tree.search(word) is None:
        tree.insert(word)
        print(tree.getSize())
        print(tree.GetHeight(tree.root))
        print(tree.BlackHeight())
    else:
        print(f"ERROR: '{word}' already in the dictionary!")

def lookUp(word,tree):
    if tree.search(word) is None:
        print("NO")
    else:
        print("YES")




