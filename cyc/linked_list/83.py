# 83.py -- Remove Duplicates from Sorted List

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    ans = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return ans