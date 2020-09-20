# 104.py -- Maximum Depth of Binary Tree

'''
Description:
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
Depth is 3
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        '''
        pretty fast,
        but need maintain a list.
        '''
        if not root:
            return 0
        def dfs(node, dep, deps):
            if not node.left and not node.right:
                deps.append(dep)
                return
            if node.left:
                dfs(node.left, dep+1, deps)
            if node.right:
                dfs(node.right, dep+1, deps)
        deps = []
        dfs(node, 0, deps)
        return max(deps)

    def maxDepth(self, root):
        '''
        do not need to maintain a list
        but little slower because need to call max every recursion.
        '''
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        