# 101.py -- Symmetric Tree

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        
        # create a function which can check the left and right node of a father node compared with
        # the mirror father node
        def dfs(l, r):
            if not l or not r: return False
            if not l and not r: return True
            if l.val == r.val:
                return dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root, root)
