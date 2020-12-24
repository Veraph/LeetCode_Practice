class Solution {
public:
    // using map
    // space O(n), time O(n)
    Node* copyRandomList(Node *head) {
        if (!head) return nullptr;
        map<Node*, Node*> nodeMap;

        Node* cur = head;
        // build the map
        while (cur) {
            nodeMap[cur] = new Node (cur -> val);
            cur = cur -> next;
        }
        cur = head;

        // create the relationships in newly built list
        while (cur) {
            nodeMap[cur] -> next = nodeMap[cur -> next];
            nodeMap[cur] -> random = nodeMap[cur -> random];
            cur = cur -> next;
        }
        return nodeMap[head];
    }

    // add and divide the original lists without additional space
    // space O(1), time O(n)
    Node* copyRandomList(Node *head) {
        if (!head) return nullptr;
        
        Node *cur = head;
        // first loop to copy a new lists with next elements
        while (cur) {
            Node *tmp = new Node(cur -> val);
            tmp -> next = cur -> next;
            cur -> next = tmp;
            cur = tmp -> next;
        }
        cur = head;

        // second loop to copy the random loop
        while (cur) {
            if (cur -> random)
            cur -> next -> random = cur -> random -> next;
            cur = cur -> next -> next;
        }

        cur = head -> next;
        // split the huge list into two
        Node *res = head -> next, *pre = head;
        while (cur -> next) {
            // the order is important
            pre -> next = pre -> next -> next;
            cur -> next = cur -> next -> next;
            pre = pre -> next;
            cur = cur -> next;
        }
        pre -> next = nullptr;
        return res;
    }
};
