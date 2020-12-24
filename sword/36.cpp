class Solution {
public:
    // recursive
    Node *pre, *head;
    Node *treeToDoublyList(Node *root) {
        if (!root) return nullptr;
        dfs(root);
        // connect the begin and the end of the list
        head -> left = pre;
        pre -> right = head;
        return head;
    }

    void dfs(Node cur) {
        // inorder traversal
        // from small to big
        if (!cur) return;
        dfs(cur -> left);
        if (pre) pre -> right = cur;
        else head = cur;
        cur -> left = pre;
        pre = cur;
        dfs(cur -> right);
    }

};
