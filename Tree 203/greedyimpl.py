#Node blueprint
class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val

    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left

    def getVal(self):
        return self.value


#       5
#   12      28
# 99   33  7   9

#Creating tree
tree = Node(5)
tree.left = Node(12)
tree.left.left = Node(99)
tree.left.right = Node(33)
tree.right = Node(29)
tree.right.left = Node(7)
tree.right.right = Node(9)

#Greedey Implementation
def greedy(self):
    if(self!=None):
        if(self.left.getVal() > self.right.getVal()):
            greedy(self.left)
        else:
            greedy(self.right)
    else:
        return self.getVal()

print(greedy(tree))