class Solution {
public:
    // time O(n)
    vector<int> inorder;
    int kthLargest(TreeNode* root, int k) {
          dfs(root, inorder);
          return inorder[inorder.size() - k];
    }

    void dfs(TreeNode* root, vector<int> &inorder) {
        if (!root) return;

        dfs(root -> left, inorder);
        inorder.push_back(root -> val);
        dfs(root -> right, inorder);
    }


    // optimize, do not use vector
    // and quit recursion in advance
    // use the reverse of inorder
    int res, idx;
    int kthLargest(TreeNode* root, int k) {
        idx = k;
        dfs(root);
        return res;
    }

    void dfs(TreeNode* root) {
        if (!root || !idx) return;
        dfs(root -> right);
        if (! (--idx)) {
            res = root -> val;
            return;
        }
        dfs(root -> left);
    }
};
