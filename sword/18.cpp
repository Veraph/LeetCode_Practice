

class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val) {
        if (!head) return head;
        if (head->val == val) return head->next;

        ListNode* cur = head;
        while (cur->next && cur->next->val != val) {
            cur = cur->next;
        }
        if (cur->next) {
            cur->next = cur->next->next;
        }

        return head;
    }
};
