// Loop twice
class Solution {
public:
    ListNode *getKthFromEnd(ListNode *head, int k) {
        if (head == NULL) {
            return head;
        }

        ListNode *cpy = head;
        int cnt = 0;
        while(cpy != NULL) {
            cpy = cpy->next;
            cnt++;
        }

        if (k > cnt) {
            return head;
        }
        while(cnt != k) {
            head = head->next;
            cnt--;
        }
        return head;
    }
}
// Loop one time
// using two pointer
// becareful about the robustness of your code
class Solution {
public:
    ListNode *getKthFromEnd(ListNode *head, int k) {
        // 1.if head is nullptr, the program will crash
        // 2. if k is 0, the program will crash
        if (head == nullptr || k == 0) {
            return nullptr;
        }

        ListNode *ptr1 = head;
        for (int i = 1; i < k; ++i) {
            // 3. if the total number of nodes less than k - 1
            // the program will crash
            if (ptr1->next != nullptr)
                ptr1 = ptr1->next;
            else
                return nullptr;
        }
        ListNode *ptr2 = head;
        while (ptr1->next != nullptr) {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        return ptr2;
    }
};




