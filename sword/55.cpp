class Solution {
public:
    // recursion
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root -> left), maxDepth(root -> right)); 
    }


    // iteration
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int res = 0;
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        while (!nodeQue.empty()) {
            int sz = nodeQue.size();
            while (sz--) {
                TreeNode* cur = nodeQue.front(); nodeQue.pop();
                if (cur -> left) nodeQue.push(cur -> left);
                if (cur -> right) nodeQue.push(cur -> right);
            }
            res++;
        }
        return res;
    }
};
