# 109.py -- Convert Sorted List to Binary Search Tree

'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    # convert to lists first
    nums = []
    while head:
        nums.append(head.val)
        head = head.next

    def dfs(nums, start, end):
        if start > end: return
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = dfs(nums, start, mid - 1)
        root.right = dfs(nums, mid + 1, end)
        return root
    
    return dfs(nums, 0, len(nums) - 1)

    '''
    pure linked list operation
    using the mid point find method of linked list
    same speed as the first one,
    but do not have an extra O(n) space used for list building
    '''
    def premid(head):
        # find the point before mid
        slow = head
        pre = head
        fast = head.next
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre
    
    if not head: return
    # when reach the end of linked list
    if not head.next:
        return TreeNode(head.val)
    premid = premid(head)
    mid = premid.next
    # cut the linked list
    premid.next = None
    # create the node
    root = TreeNode(mid.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(mid.next)
    return root

    '''
    simpler linked list operation method
    the difference is that the method tries to build the BST
    from the start of the linked list
    '''
    def findsize(head):
        ptr = head
        siz = 0
        while ptr:
            siz += 1
            head = head.next
        return siz
    
    size = findsize(head)

    def convert(l, r):

        # need this
        nonlocal head

        if l > r: return None

        mid = (l + r) // 2
        
        left = convert(l, mid - 1)
        node = TreeNode(head.val)
        node.left = left
        head = head.next
        node.right = convert(mid + 1, r)
        return node
    
    return convert(0, size - 1)


