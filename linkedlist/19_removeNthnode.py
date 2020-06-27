# Define a singly-linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # generate three pointers
        fast = slow = head
        for _ in range(n):
            # let fast pointer run to the index of n
            fast = fast.next
        if not fast:
            # if fast pointer point to None
            # the n is the length, hence first value delete
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        # drop the slow.next one
        slow.next = slow.next.next
        return head   