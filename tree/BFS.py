# using 'binary tree level order traversal' leetcode problem as example

# given the root of a binary tree, return the level order traversal of its nodes' values.
# from left to right, level by level
# input: root = [3,9,20,null,null,15,7]
# output: [[3],[9,20],[15,7]]

# need a queue data structure to implement a BFS, first in, first out

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def breadth_first_search(root):
    if not root:
        return []

    queue = [root]
    result = []

    while queue:
        level_values = []
        n = len(queue)

        for _ in range(n):
            node = queue.pop(0)
            level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_values)

    return result

# LeetCode 199 Binary Tree Right-Side View : Medium
# Given a Binary tree, imagine yourself standing on 
# the right side of it, return the values of the nodes 
# you can see ordered from top to bottom.

# for every level in a tree we want the right most leaf
# impliment with a queue data structure
def right_side_view(root):
    res = []
    q = collections.deque([root])

    while q:
        right_side = None
        qlen = len(q)

        for i in range(qlen):
            node = q.popleft()
            if node:
                right_side = node
                q.append(node.left) # left node before the right node
                q.append(node.right)

        if right_side:
            res.append(right_side.val)
    
    return res

if __name__ == "__main__":

    # Example usage:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)

    print(breadth_first_search(root))  # Output: [[3], [9, 20], [15, 7]]
    print(right_side_view(root1))