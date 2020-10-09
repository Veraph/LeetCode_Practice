# 501.py -- Find mode in BST

'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root):
    '''
    method 1
    used some space
    '''
    if not root: return
    # do the inorder to form the num list
    nums = []
    def inorder(node):
        if node:
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
    inorder(root)

    # create res list to store the frequency
    res = []
    s, e = 0, 0
    while e < len(nums):
        if e == len(nums) - 1:
            res.append((nums[e], e - s + 1))
            break
        if nums[e + 1] == nums[e]:
            e += 1
        else:
            res.append((nums[e], e - s + 1))
            s = e + 1
            e = s
    res.sort(key = lambda x: x[1], reverse = True)

    # generate the ans list
    ans = [res[0][0]]
    for val, freq in res[1:]:
        if freq == res[0][1]:
            ans.append(val)
    return ans

    '''
    Method 2
    The real O(1) space method
    do the two passes(use the inorder func twice)
    '''
    def inorder(node):
        if node:
            inorder(node.left)
            helper(node.val)
            inorder(node.right)
    
    # used to find the maximum freq one
    def helper(val):
        if val != self.currVal:
            self.currVal = val
            self.currCnt = 0
        self.currCnt += 1

        if self.currCnt > self.maxCnt:
            self.maxCnt = self.currCnt
            self.modeCnt = 1
        elif self.currCnt == self.maxCnt:
            if self.flag:
                modes[self.modeCnt] = self.currVal
            self.modeCnt += 1
    
    self.currVal, self.currCnt, self.maxCnt, self.modeCnt, self.flag = float('inf'), 0, 0, 0, False
    inorder(root)
    modes = [float('inf')] * self.modeCnt
    self.modeCnt, self.currCnt, self.flag = 0, 0, True
    inorder(root)
    return modes

    



        
