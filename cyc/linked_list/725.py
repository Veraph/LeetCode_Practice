# 725.py -- Split Linked List in Parts

'''
Description:
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(root, k):
        cnt = 0
        cur = root
        while cur:
            cnt += 1
            cur = cur.next
        
        res = []
        # cnt <= k
        if cnt <= k:
            # be careful about the edge case
            if root:
                a, b = root, root.next
                while a:
                    a.next = None
                    res.append(a)
                    a = b
                    if a:
                        b = b.next
            for _ in range(k - cnt):
                res.append(None)

        # cnt > k
        else:
            # create the list the store the ans situation
            num = cnt // k
            remain = cnt % k
            method = [num for _ in range(k)]

            i = 0
            while remain:
                method[i] += 1
                remain -= 1
                i += 1

            # generate ans
            a = root
            b = a
            for i in method:
                while i - 1:
                    b = b.next
                    i -= 1
                ptr = b.next
                b.next = None
                res.append(a)
                a = b = ptr

        return res
            
            
