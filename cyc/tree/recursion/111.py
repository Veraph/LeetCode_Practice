# 111.py -- Minimum Depth of Binary Tree

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        '''
        BFS
        '''
        if not root:
            return 0

        cnt = 1
        stack = [(root, cnt)]
        for i in stack:
            if not i[0].left and not i[0].right:
                return i[1]
            if i[0].left:
                stack.append((i[0].left, i[1] + 1))
            if i[0].right:
                stack.append((i[0].right, i[1] + 1))

        '''
        DFS
        '''
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # be careful that the distance is from the root down to the leaf!
        if left == 0 or right == 0:
            return left + right + 1
        return min(left, right) + 1