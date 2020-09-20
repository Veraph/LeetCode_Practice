# 160.py -- Intersection of Two Linked Lists

'''
Description:
Write a program to find the node at which the intersection of two singly linked lists begins.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pa = headA
        pb = headB

        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next

        return pa