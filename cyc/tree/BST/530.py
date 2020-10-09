# 530.py -- Minimum Absolute Difference in BST

'''
Given a binary search tree with non-negative values, 
find the minimum absolute difference between values of any two nodes.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    '''
    method 1
    use inorder travelsal
    and calculate the differences
    '''
    nums = []
    def inorder(node):
        if node:
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

    inorder(root)
    ans = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    return min(ans)

    