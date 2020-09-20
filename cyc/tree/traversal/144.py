# 144.py -- Binary Tree Preorder Traversal

'''
Description:
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(root):
        '''
        dfs
        '''
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return res

        '''
        iterate(BFS)
        simulate stack
        '''
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                node = stack.pop()
                stack.append(node.right)
                stack.append(node.left)
                res.append(node.val)
        return res
