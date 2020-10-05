# 112.py -- Path Sum

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(root, sum):
        if root:
            if root.val == sum and not root.left and not root.right:
                return True

            '''
            return a or b:
            equals to 
            if a:
                return a
            if b:
                return b
            '''
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        return False