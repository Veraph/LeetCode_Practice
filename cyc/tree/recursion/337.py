# 337.py -- House Robber III

'''
Description:
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        '''
        modify the original structure to speed up.
        compare the val between skip this point or not skip.
        '''
        if not root:
            return 0
        def dfs(root):
            if not root:
                return (0,0)
            left = dfs(root.left)
            right = dfs(root.right)
            return (root.val+left[1]+right[1], max(left[0],left[1])+ max(right[0], right[1]))
        return max(dfs(root))

        '''
        TLE, 
        too many recursions to call
        '''
        if not root:
            return 0
        
        val1, val2= root.val, 0
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        val2 += self.rob(root.left) + self.rob(root.right)
        
        return max(val1, val2)