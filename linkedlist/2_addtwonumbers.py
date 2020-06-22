# define linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# my first think: store l1 and l2 into two lists respectively
# then get the length of the list, and times 10 to the power of n (n < length)
# and the add the two int, create a new linked list, return
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # it is like the (v1+v2+carry) % 10
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

