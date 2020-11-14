#include <iostream>
#include <stack>

using std::cin, std::cout, std::endl;

//print linked list from end to begin
struct ListNode {
    int val;
    ListNode *next;
}

std::vector<int> reverse(ListNode *head) {
    std::vector<int> res;
    std::stack<ListNode*> nodes;
    ListNode *pNode = head;
    while (pNode != NULL) {
        nodes.push(pNode);
        pNode = pNode->next;
    }
    while (!nodes.empty()) {
        res.push_back(nodes.top()->val);
        nodes.pop();
    }
    return res;
}

//the recursive version
//the recursive is actually a stack structure
std::vector<int> reverse1(ListNode *head) {
    if (!head)
        return {};
    std::vector<int> nodes = reverse1(head->next);
    nodes.push_back(head->val);
    return nodes;
}
