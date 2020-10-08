# 108.py -- Convert Sorted Array to Binary Search Tree

'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    '''
    continually find out the mid index
    of remaining array to construct
    the BST
    '''
    def dfs(nums, start, end):
        # AGAIN!
        # do not dive into the details
        # just write the abstraction
        if start > end: return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = dfs(nums, start, mid - 1)
        root.right = dfs(nums, mid + 1, end)
        return root

    dfs(nums, 0, len(nums) - 1)
    return root
