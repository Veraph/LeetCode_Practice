# 437.py -- Part Sum III

'''
Description:
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    it is infact a recursion that loop through every node as a root.
    '''
    def pathSum(self, root, sum):
        '''
        The hard part is that
        we should let the begin index
        starts at any position
        '''
        if not root: return 0
        
        def dfs(node, sum):
            if not node: return 0
            subcnt = 0
            if node.val == sum:
                subcnt += 1
            # sum up the all possiblilities start from the specific node
            subcnt += dfs(node.left, sum - node.val) + dfs(node.right, sum - node.val)
            return subcnt
            
        # the loop operation which regards every node as a start point
        cnt = dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return cnt

    '''
    dfs with memorization
    '''
    def pathSum(self, root, sum):
        if not root: return 0

        self.cnt = 0
        # create a cache to memory the sum of nodes we visited
        cache = {0:1}

        def dfs(node, target, curPathSum, cache):
            if not root: return
            # calculate the current path sum and old one
            curPathSum += node.val
            oldPathSum = curPathSum - target
            # if old one exist in the dict, means we can achieve the target
            self.cnt += cache.get(oldPathSum, 0)
            # add the current path sum to the dict, if not, create a new one with val 1
            cache[curPathSum] = cache.get(curPathSum, 0) + 1

            # go down the tree
            dfs(node.left, target, curPathSum, cache)
            dfs(node.right, target, curPathSum, cache)
            # when we finish this branch, the current one unavailable, remove this one
            cache[curPathSum] -= 1

        dfs(root, sum, 0, cache)
        return self.cnt
