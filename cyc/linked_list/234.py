# 234.py -- Palindrome Linked List

'''
Given a singly linked list, determine if it is a palindrome.
'''

class ListNode:
    def __init__(self, val=0, next=val):
        self.val = val
        self.next = next

class Solution:
    '''
    Space O(N)
    '''
    def isPalindrome(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res == res[::-1]

    '''
    Space O(1)
    cut the original list in half, reverse the second half and compare
    '''
    def isPalindrome(head):

        # deal with edge case
        if not head or not head.next:
            return True

        # find the cut position slow 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # when we have even num of nodes
        # don't bother when we have odd
        if fast:
            slow = slow.next

        # do the cut
        ptr = head
        while head.next != slow:
            head = head.next
        head.next = None

        # reverse the second half
        pre = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = pre
            pre = curr
        
        # compare the two list
        while pre and ptr:
            if pre.val != ptr.val:
                return False
            pre = pre.next
            ptr = ptr.next

        return True


