# 538.py -- Convert BST to greater Tree

'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root):
    '''
    inorder first
    and do the culmulative addition
    '''

    res = []
    def inorder(root):
        if root:
            inorder(root.left)
            res.append(root)
            inorder(root.right)
    # do the inorder operation
    inorder(root)
    # add values
    for i in range(len(res) - 2, -1, -1):
        res[i].val += res[i + 1].val
    
    return root

    '''
    simpler
    iterate right subtree first
    '''
    self.sum = 0

    def dfs(root):
        if not root: return
        dfs(root.right)
        self.sum += root.val
        root.val = self.sum
        dfs(root.left)

    dfs(root)
    return root