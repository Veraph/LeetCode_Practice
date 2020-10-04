# 445.py -- Add Two Numbers II

'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1, l2):
        # generate three lists
        list_a = []
        list_b = []
        while l1:
            list_a.append(l1.val)
            l1 = l1.next
        while l2:
            list_b.append(l2.val)
            l2 = l2.next

        res = [0 for i in range(max(len(list_a), len(list_b))+1)]

        # do the calculation
        carry = 0
        index = -1
        # be careful about the add implementation
        while list_a or list_b or carry:
            if list_a:
                carry += list_a.pop()
            if list_b:
                carry += list_b.pop()

            res[index] = carry % 10
            carry //= 10
            index -= 1

        # generate the new 
        if res[0] = 0:
            res = res[1:]
        node = ListNode(res[0])
        ptr = node
        for i in range(1, len(res)):
            ptr.next = ListNode(res[i])
            ptr = ptr.next

        return node





        
