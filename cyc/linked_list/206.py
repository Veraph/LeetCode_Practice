# 206.py -- Reverse Linked List

'''
Description:
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        '''
        Recursive
        '''
        def reverse(node, prev=None):
            if not node:
                return prev
            n = node.next
            node.next = prev
            return reverse(n, node)

        reverseList(head)

    def reverseList2(self, head):
        '''
        Iterately, with same speed O(n)
        '''
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev