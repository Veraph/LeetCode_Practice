# 328.py -- Odd Even Linked List

'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenLisr(head):
    '''
    have to be in place
    draw carefully
    '''

    if head and head.next:
        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd.next.next = even_head
            odd = odd.next
            even = even.next

    return head