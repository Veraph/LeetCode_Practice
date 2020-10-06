# 572.py -- Subtree of another tree

'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s, t):
        '''
        BFS
        wrong, because we are comparing the difference of val, not the tree itself(address).
        '''
        queue = [s]
        while queue:
            for i in queue:
                if i == t:
                    return True
                queue.append(s.left)
                queue.append(s.right)
        return False

        '''
        DFS
        have to create an additional dfs call to deal with [1,1], [1] situation.
        '''
        if not s:
            return False
        return dfs(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        def dfs(s, t):
            if not s and not t: return True
            if not s or not t: return False
            if s.val != t.val: return False
            
            return dfs(s.left, t.left) and dfs(s.right, t.right)

        

