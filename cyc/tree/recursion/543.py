# 543.py -- Diameter of Binary Tree

'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        
        # add variable
        self.cnt = 0

        def dfs(node):
            if not node: return 0 # we are counting the connnections
            l, r = dfs(node.left), dfs(node.right)
            self.ans = max(self.ans, l + r)

            return 1 + max(l, r)

        
        dfs(root)
        return self.cnt
    