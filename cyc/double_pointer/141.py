# 141.py -- Linked list cycle

'''
Description:
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory
'''

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    '''
    use the two pointer thinking to save time.
    (a fast pointer and a slow pointer)
    take care of border case!
    maintain a list to store is slow baby.
    '''
    if not head:
        return None
    ptr1 = head
    ptr2 = head.next
    while ptr1 and ptr2 and ptr2.next:
        if ptr1 == ptr2:
            return True
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
    return False

        