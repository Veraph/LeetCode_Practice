# 404.py -- Sum of Left Leaves

'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        self.cnt = 0
        
        def dfs(root, l):
            if root:
                # only cnt the left LEAVES!
                if l and not root.left and not root.right:
                    self.cnt += root.val

                dfs(root.left, 1)
                dfs(root.right,0)
                
        dfs(root, 0)
        return self.cnt

        '''
        without additional function
        '''
        if not root: return 0
        # conditions to ensure is a left leave
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) 
                
            
