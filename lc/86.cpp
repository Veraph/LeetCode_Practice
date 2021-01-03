class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *big = new ListNode(0);
        ListNode *auxBig = big;
        ListNode *small = new ListNode(0);
        ListNode *auxSmall = small;
        while (head) {
            if (head -> val >= x) {
                big -> next = head;
                big = big -> next;
            } else {
                small -> next = head;
                small = small -> next;
            }
            head = head -> next;
        }
        big -> next = nullptr;
        small -> next = auxBig -> next;
        return auxSmall -> next;
    }
};
