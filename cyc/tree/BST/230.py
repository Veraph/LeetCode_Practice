# 230.py -- Kth Smallest Element in a tree

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    '''
    Use BFS,
    however it is not good
    as we may modify the tree frequently
    '''
    queue = [(root, root.val)]
    for node, val in queue:
        if node.left:
            queue.append((node.left, node.left.val))
        if node.right:
            queue.append((node.right, node.right.val))

    queue.sort(key = lambda x: x[1])
    return queue[k-1][1]

    '''
    Remember it is a BST,
    the left child is less than father
    the right child is bigger than father
    Try Inorder
    '''
    self.cnt = 0
    self.val = 0

    def inorder(node, k):
        if not node:
            return
        inorder(node.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.val = node.val
        inorder(node.right, k)

    inorder(root, k)
    return self.val