# 513.py -- Find Bottom Left Tree Value

'''
Given a binary tree, find the leftmost value in the last row of a tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root):
    '''
    use BFS
    '''
    stack = [(root, 1)]
    for node, dep in root:  
        if not node.left and not node.right:
            continue
        if node.left:
            stack.append((node.left, dep + 1))
        if node.right:
            stack.append((node.right, dep + 1))

    stack.sort(key = lambda x: x[1], reverse = True)
    return stack[0][0].val

    '''
    Optimization
    '''
    stack = [root]
    res = 0
    while stack:
        node = stack.pop(0)
        res = node.val
        # add right first
        # then the final res will be the leftmost in the 
        # last row
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

    '''
    use deque
    no big difference in speed
    '''
    queue = collections.deque()
    q.append(root)
    node = q.popleft()
