# 19.py -- Remove Nth Node from End of List

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        '''
        recursively
        '''
        # create a node before head to deal with extreme situation like [1]
        cur = ListNode(0)
        cur.next = head
        
        def recur(cur, n):
            if cur.next: 
				# add cnt to let it equal to n eventually
                cnt = 1 + recur(cur.next, n)
                if cnt == n:
					# delete the expected node
                    cur.next = cur.next.next
            else:
				# reach the tail, return 0
                return 0           
            return cnt

        recur(cur, n)
		# we do not need the node we created, hence return the next
        return cur.next

        '''
        iterately
        '''
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in xrange(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next



