// recursion
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        
        ListNode *ans = nullptr;

        if (l1 -> val < l2 -> val) {
            ans = l1;
            ans -> next = mergeTwoLists(l1 -> next, l2);
        } else {
            ans = l2;
            ans -> next = mergeTwoLists(l1, l2 -> next);
        }
        return ans;
    }
};

// iterate
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if (!l1) return l2;
        if (!l2) return l1;

        ListNode *ans = new ListNode(0);
        ListNode *cur = ans;

        while (l1 && l2) {
            if (l1 -> val < l2 -> val) {
                cur -> next = l1;
                l1 = l1 -> next;
            } else {
                cur -> next = l2;
                l2 = l2 -> next;
            }
            cur = cur -> next;
        }

        cur -> next = (!l1) ? l2 : l1;
        cur = ans -> next;
        delete ans;
        return cur;
    }
};
