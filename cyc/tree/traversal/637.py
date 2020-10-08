# 637.py -- Average Levels in Binary Tree

'''
Description:
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        '''dfs'''
        res = []
        def dfs(node, depth):
            if node:
                if len(res) <= depth:
                    res.append([0,0])
                res[depth][0] += node.val
                res[depth][1] += 1
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)

        return [s/n for s, n in res]

        '''
        bfs
        better both in space and time
        '''
        res = []
        current_level = [root]

        while current_level:
            level_val = 0
            next_level = []

            for node in current_level:
                level_val += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            res.append(level_val / len(current_level))
            current_level = next_level
            
        return res
            



