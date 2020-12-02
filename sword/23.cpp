class Solution {
public:
    ListNode* MeetingNode(ListNode *phead) {
        // THE ROBUTNESS!!!
        if (phead == nullptr)
            return nullptr;

        ListNode *pSlow = phead -> next;
        if (pSlow == nullptr)
            return nullptr;

        ListNode *pFast = pSlow -> next;
        while (pFast != nullptr && pSlow != nullptr) {
            if (pFast == pSlow)
                return pFast;

            pSlow = pSlow -> next;

            pFast = pFast -> next;
            if (pFast != nullptr)
                pFast = pFast -> next;

        }
        return nullptr;
    }

    ListNode* EntryNodeOfLoop(ListNode *phead) {
        ListNode *meetingNode = MeetingNode(phead);
        
        // cnt how many node in the loop
        int loopNode = 1;
        ListNode *pNode1 = meetingNode -> next;
        while (pNode1 != meetingNode) {
            pNode1 = pNode1 -> next;
            loopNode++;
        }
        
        // then we can calculate the entry point
        pNode1 = phead;
        ListNode *pNode2 = phead;
        for (int i = 0; i < loopNode; i++) {
            pNode1 = pNode1 -> next;
        }
        while (pNode1 != pNode2) {
            pNode1 = pNode1 -> next;
            pNode2 = pNode2 -> next;
        }

        return pNode1;
    }
};





