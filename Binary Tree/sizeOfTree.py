#   
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# FUNCTION TO GET SIZE OF NODE
def size(node):

    # if Node is empty return 0
    if node is None:
        return 0
    
    else:

        # calculating the total size 
            #Left part + 1[root node ] + Right part
        return (size(node.left)+1 + size(node.right) )


# MAKING THE TREE WITH THE GIVEN NODES DATA
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left  = Node(4) 
root.left.right = Node(5) 
  
#printing the size of Tree
print ("Size of the tree is %d" %(size(root)))