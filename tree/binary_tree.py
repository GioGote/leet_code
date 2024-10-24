'''
Binary Tree: a data structure in which each node has at most two children, which are referred to as the 
left child and right child.
'''

# define a binary tree
class Node(object):
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__ (self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
        
    '''
    Pre-Order Traversal:
    1. Check if the current node is empty / null
    2. Display the data part of the root
    3. Traverse the left subtree by recursively calling the pre-order function
    4. Traverse the right subtree by recursively calling the pre-order function

    PRE-ORDER: F, B, A, D, C, E, G, I, H
                F
             /    \
           B       G
          / \       \
         A   D       I
            / \      /
            C  E    H
    ''' 

    def preorder_print(self, start, traversal):
        # root -> left -> right

        if start:
            traversal += (str(start.value) + "-") # formatter
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal
    
    '''
    In-Order Traversal:
    1. Check if the current node is empty / null
    2. Traverse the left subtree by recursively calling the in-order function
    3. Display the data part of the root (or current node)
    4. Traverse the right subtree by recursively calling the in-order function

    IN-ORDER: A, B, C, D, E, F, G, H, I
                F
             /    \
           B       G
          / \       \
         A   D       I
            / \      /
            C  E    H
    '''

    def inorder_print(self, start, traversal):
        # left -> root -> right

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        
        return traversal
    
    '''
    Post-Order Traversal:

    POST-ORDER: A, C, E, D, B, H, I, G, F
                F
             /    \
           B       G
          / \       \
         A   D       I
            / \      /
            C  E    H
    '''

    def postorder_print(self, start, traversal):
        # left -> right -> root 

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))

# 1-2-4-5-3-6-7-8-

print(tree.print_tree("inorder"))

# 4-2-5-1-6-3-7-8-

print(tree.print_tree("postorder"))

# 4-2-5-6-3-7-8-1-

# Tree Traversal
# Depth First Search: Pre-order, in-order, post-order