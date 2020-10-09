# 653.py -- Two Sum IV - input is a BST

'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    '''
    method 1
    transfer to a list and solve it like a two sum
    '''
    # transfer to list with simple loop
    nums = []
    remain = [root]
    while remain:
        node = remain.pop(0)
        nums.append(node.val)
        if node.left:
            remain.append(node.left)
        if node.right:
            remain.append(node.right)
    nums.sort()

    # we can do the transfer using inorder traversal
    # because it is a BST, and the nums we get from inorder
    # is a sorted nums
    # the result is slightly faster than previous one
    # but it used more space
    # and still not faster than the method 2
    def inorder(node):
        if node:
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)


    # do the formal two sums
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > k:
            r -= 1
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            return True
    return False

    '''
    method 2
    loop through the BST,
    create set to store the val visited
    and it is indeed faster
    '''
    queue, visited = [root], set()
    for node in queue:
        if k - node.val in visited:
            return True
        visited.add(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
