# 687.py -- Longest Univalue Path

'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.
Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root):
        '''
        like diameter of binary tree
        '''
        self.cnt = 0

        def dfs(root):
            if not root: return 0
            # go down until reach the None, then can start to calculate
            left, right = dfs(root.left), dfs(root.right)

            left_len = left + 1 if root.left and root.left.val == root.val else 0
            right_len = right + 1 if root.right and root.right.val == root.val else 0
            self.cnt = max(self.cnt, left_len + right_len)

            # return the current maximum length as the left or right value in previous stack call
            return max(left_len, right_len)

        dfs(root)
        return self.cnt


