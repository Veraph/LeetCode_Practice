# 94.py -- Binary Tree Inorder Traversal

'''
Middle items first
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        '''DFS'''
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        return res


        '''BFS'''
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right