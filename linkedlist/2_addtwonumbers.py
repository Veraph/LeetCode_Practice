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
        # carry is a dummy which can only be 0 or 1 because 9+9 can only be 18
        carry = 0
        # what are root and n here? is it create the first digits of the result linked list?
        # here root and n express the address of the new listnode(0)
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                # take the value of first node of l1 and store it in v1
                v1 = l1.val
                # l1 is originally an node with value 2, and the address points to None 
                # now l1 becomes the node with value 4, 
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # it is like the (v1+v2+carry) % 10
            carry, val = divmod(v1+v2+carry, 10)
            # let the n(listnode(0)) point to new node listnode(7)
            n.next = ListNode(val)
            # change the n from listnode(0) to listnode(7)
            n = n.next
        # root and n are two different pointers, the root always point at the beginning, which is the listnode(0), 
        # however, the n keeps moving to connect the whole lists
        # hence, in this example, return root.next, will return the address of 7, and 7 connects the 0 and the 8,
        # which is the answer linked lists
        print(root.next)
        return root.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    Solution().addTwoNumbers(l1, l2)

