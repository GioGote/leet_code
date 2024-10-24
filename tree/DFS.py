class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode 104: Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth
# input: root = [3,9,20,null,null,15,7]
# output: 3

def depth_first_search(root):
    if not root:
        return 0
    
    return 1 + max(depth_first_search(root.left), depth_first_search(root.right))

# leet code 110 Balanced Binary Tree
# given a binary tree, determine if it is height-balanced
# O(n)
def is_balanced(root):
    # do it recusively
    def dfs(root):
        if not root:
            return [True, 0]
        
        left, right = dfs(root.left), dfs(root.right)
        balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        return [balance, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]

# 1448 Count Good Nodes in Binary 
# Given a binary tree rootm a node X in the tree is named good if in the path from root to X
# there are no nodes with a value greater than X
# return the number of good nodes in the binary tree
# using Pre-order
def good_nodes(root):
    def dfs(node, maxVal):
        if not node:
            return 0
        
        # non-empty node
        res = 1 if node.val >= maxVal else 0 # we have 1 good node if node.val is greater than or equal to maxVal
        maxVal = max(maxVal, node.val) # updating the maxVal
        res += dfs(node.left, maxVal) # recursive call on left child | count number of good nodes
        res += dfs(node.right, maxVal) # recursive call on right child | count number of good nodes
        return res
    
    return dfs(root, root.val)

# Invert a Binary tree using DFS
# visit every single node and swap the two positions of its children
def invert_binary_tree(root): # POPULAR QUESTION
    if not root:
        return None
    
    #swap children
    tmp = root.left # Store left child value in a temp variable
    root.left = root.right
    root.right = tmp

    # Now invert the subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

def merge_trees(tree1, tree2):
    if not tree1 and not tree2:
        return None
    
    v1 = tree1.val if tree1 else 0 # assign value to v1 if tree1.val is there, if not, assign 0
    v2 = tree2.val if tree2 else 0 # same thing but just for tree2
    root = TreeNode(v1 + v2)

    root.left = merge_trees(tree1.left if tree1 else None, tree2.left if tree2 else None)
    root.right = merge_trees(tree1.right if tree1 else None, tree2.right if tree2 else None)

    return root

# Print out binary tree values IN ORDER
def level_order_traversal(root):
    if not root:
        return
    
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)

    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(9)

    root_merge1 = TreeNode(1)
    root_merge1.left = TreeNode(3)
    root_merge1.right = TreeNode(2)
    root_merge1.left.left = TreeNode(5)

    root_merge2 = TreeNode(2)
    root_merge2.left = TreeNode(1)
    root_merge2.right = TreeNode(3)
    root_merge2.left.right = TreeNode(4)
    root_merge2.right.right = TreeNode(7)


    print(depth_first_search(root))
    print(is_balanced(root))
    print(good_nodes(root1))
    invert_binary_tree(root2)
    level_order_traversal(root2)
    print("\n")
    merged_trees = merge_trees(root_merge1, root_merge2)
    level_order_traversal(merged_trees)