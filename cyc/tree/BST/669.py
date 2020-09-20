# 669.py -- Trim a Binary Search Tree

'''
Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so that all its elements lies in [low, high]. 
You might need to change the root of the tree, 
so the result should return the new root of the trimmed binary search tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    do not need to think about too much detail about the recersive formular itself.
    think about the things you want!
    the logic is more important!
    '''
    def trimBST(self, root, low, high):
        if not root: return root
        if root.val > high: return self.trimBST(root.left, low, high)
        if root.val < low: return self.trimBST(root.right, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
    
        return root