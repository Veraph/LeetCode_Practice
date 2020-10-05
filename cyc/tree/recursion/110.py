# 110.py -- Balanced Binary Tree

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):

    '''
    becareful abou the case [1,2,2,3,null,null,3,4,null,null,4]
    '''
    if not root: return 1
    l = isBalanced(root.left)
    if not l: return # forbid to go the right sub tree if left is empty
    r = isBalanced(root.right)
    if not r: return
    '''
    below code same as:
    if abs(l - r) <= 1:
        return 1 + max(l, r)
    else:
        return abs(l - r) <= 1
    '''
    return abs(l - r) <= 1 and 1 + max(l, r)