# 617.py -- Merge two Binary Trees

'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1, t2):
        '''
        create a new tree
        think more abstractly
        ''''
        if not t1 and not t2:
            return None
        if not t1: return t2
        if not t2: return t1
        
        t3 = TreeNode(t1.val + t2.val)
        t3.left = mergeTrees(t1.left, t2.left)
        t3.right = mergeTrees(t1.right, t2.right)

        return t3
        
        
