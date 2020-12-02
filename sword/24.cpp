// method1
// iteration
class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        ListNode *pre = nullptr;
        ListNode *pos = head;

        while (head != nullptr) {
            pos = pos -> next;
            head -> next = pre;
            pre = head;
            head = pos;
        }
        return pre;
    }

};

// method2
// recursion
class Solution {
public:
    ListNode *node = nullptr;
    ListNode *reverseList(ListNode *head) {
        if (head == nullptr || head -> next == nullptr)
            return head;
        
        node = reverseList(head -> next);
        head -> next -> next = head;
        head -> next = nullptr;
        return node;
    }
};
