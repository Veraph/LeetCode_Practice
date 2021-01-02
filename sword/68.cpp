class Solution {
public:
    // recursion
    // time O(n) space O(n)
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return nullptr;
        if (root -> val > p -> val && root -> val > q -> val)
            return lowestCommonAncestor(root -> left, p, q);
        if (root -> val < p -> val && root -> < q -> val)
            return lowest CommonAncestor(root -> right, p, q);
        return root;
    }

    // iteration
    // time O(n), space O(1)
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* res = root;
        while(res) {
            if (res -> val > p -> val && res -> val > q -> val)
                res = res -> left;
            else if (res -> val < p -> val && res -> val < q -> val)
                res = res -> right;
            else
                break;
        }
        return res;
    }
};
