class Solution {
public:
    // simple recursion
    // but will duplicatively calculate nodes
    // preorder
    // from top to bottom
    bool isBalanced(TreeNode* root) {
        if (!root) return true;

        int left = maxDepth(root -> left);
        int right = maxDepth(root -> right);
        int dif = abs(left - right);
        if (dif > 1) return false;

        return isBalanced(root -> left) && isBalanced(root -> right);
    }

    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return max(maxDepth(root -> left), maxDepth(root -> right)) + 1;
    }

    // optimized recursion
    // postorder + branch cut
    // from bottom to up
    bool isBalanced(TreeNode* root) {
        return recur(root) != -1;
    }

    int recur(TreeNode* root) {
        if (!root) return 0;
        int left = recur(root -> left);
        if (left == -1) return -1;
        int right = recur(root -> right);
        if (right == -1) return -1;
        return abs(left - right) < 2 ? max(left, right) + 1 : -1;
    }
};
