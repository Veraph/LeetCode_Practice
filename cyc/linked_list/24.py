# 24.py -- Swap Nodes in Pairs

'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        '''
        do not modify straightly on the head
        '''

        ptr = ListNode(0)
        ptr.next = head
        node = ptr

        while ptr.next and ptr.next.next:
            a, b = ptr.next, ptr.next.next
            a.next = b.next
            b.next = a
            ptr.next = b
            ptr = a

        return node.next

    