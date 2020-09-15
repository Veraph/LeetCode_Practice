# 257.py -- Binary Tree Paths

'''
Description:
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    '''
    pure thinking of dfs.
    '''
    if not root:
        return []
    res = []
    def dfs(node, comb, res):
        if node.left == None and node.right == None:
            res.append(comb)
            return
        if node.left:
            dfs(node.left, comb+'->'+str(node.left.val), res)
        if node.right:
            dfs(node.right, comb+'->'+str(node.right.val), res)

    dfs(root, str(root.val), res)
    return res
        