# 95.py -- Unique Binary Search Trees II

'''
Description:
Given an integer n, generate all structurally unique BST's (binary search trees) 
that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:
0 <= n <= 8
'''
class TreeNode:
    '''
    like the 241
    use recursive to calc DC
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    def generate(l, r):
        if l == r:
            return [None]
        nodes = []
        for i in range(l, r):
            for ltree in generate(l, i):
                for rtree in generate(i+1, r):
                    node = TreeNode(i+1, ltree, rtree)
                    nodes.append(node)
        return nodes
    return generate(0, n) if n else []

