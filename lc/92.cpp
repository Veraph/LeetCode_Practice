class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* auxNode = new ListNode(-1);
        auxNode -> next = head;
        ListNode* preNode = auxNode;

        // 1. locate to the pre node before the scale
        for (int i = 0; i < left - 1; i++) {
            preNode = preNode -> next;
        }

        // 2. reverse the nodes in the scale
        ListNode* cur = preNode -> next;
        ListNode* aux;
        for (int i = 0; i < right - left; i++) {
            aux = cur -> next;
            cur -> next = aux -> next;
            aux -> next = preNode -> next;
            preNode -> next = aux;
        }
        return auxNode -> next;
    }
};
