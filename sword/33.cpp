class Solution {
public:
    // recursive
    // O(n^2)
    bool verifyPostorder(vector<int> &postorder) {
        return recur(postorder, 0, postorder.size() - 1);
    }

    bool recur(vector<int> &postorder, int l, int r) {
        if (l >= r - 1) return true;
        int cur = l;
        while (postorder[r] > postorder[cur]) cur++;
        int mid = cur;
        while (postorder[r] < postorder[cur]) cur++;

        return cur == r && recur(postorder, l, mid - 1) && recur(postorder, mid, r - 1);
    }

    // stack
    // go the order from left -> right -> root to
    // root -> right -> left;
    // O(2n) every element in and out the aux once
    bool verifyPostorder(vector<int> &postorder) {
        stack<int> aux;
        int root = INT_MAX;
        for (int i = postorder.size() - 1; i >= 0; i--) {
            if (postorder[i] > root) return false;

            while (!aux.empty() && aux.top() > postorder[i]) {
                root = aux.top();
                aux.pop();
            }

            aux.push(postorder[i]);
        }
        return true;
    }
};
