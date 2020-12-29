class Solution {
public:
    // two pointers
    // time O(m + n) space O(1)
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // edge case!
        if (!headA || !headB) return nullptr;

        ListNode *tmpA = headA;
        ListNode *tmpB = headB;
        while (tmpA != tmpB) {
            tmpA = tmpA != nullptr ? tmpA -> next : headB;
            tmpB = tmpB != nullptr ? tmpB -> next : headA;
        }
        return tmpA;
    }

    // loop to get the length
    // not that good compared with two pointers
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA = getLen(headA);
        int lenB = getLen(headB);

        int lenDif = lenA - lenB;

        ListNode *tmpLong = headA; ListNode *tmpShort = headB;

        if (lenB > lenA) {
            tmpLong = headB, tmpShort = headA;
            lenDif = lenB - lenA;
        }

        for (int i = 0; i < lenDif; i++) {
            tmpLong = tmpLong -> next;
        }

        while (tmpLong != tmpShort && tmpLong && tmpShort) {
            tmpLong = tmpLong -> next;
            tmpShort = tmpShort -> next;
        }

        return tmpLong;
    }

    unsigned int getLen(ListNode *node) {
        int len = 0;
        while (node) {
            len++;
            node = node -> next;
        }
        return len;
    }
    
};
