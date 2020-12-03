class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if (!l1) return l2;
        if (!l2) return l1;

        ListNode origin = ListNode(0);
        ListNode *res = &origin;
        ListNode *ans = &origin;
        while (l1 || l2) {
            if (!l1) {
                res = l2;
                return ans -> next;
            }

            if (!l2) {
                res = l1;
                return ans -> next;
            }

            if (cmp(l1, l2)) {
                res = l1;
                res -> next = nullptr;
                res = res -> next;
                l1 = l1 -> next;
            } else {
                res = l2;
                res -> next = nullptr;
                res = res -> next;
                l2 = l2 -> next;
            }
        }
        return ans -> next;
    }

    bool cmp(ListNode *l1, ListNode *l2) {
        return (l1 -> val) <= (l2 -> val);
    }
};
