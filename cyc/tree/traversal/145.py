# 145.py -- Binary Tree Postorder Traversal

'''
Oppsite of 144
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        '''
        dfs
        '''
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.right)
                dfs(node.left)

        dfs(root)
        return res[::-1]


        '''
        bfs
        '''
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                res.append(node.val)
        return res[::-1]