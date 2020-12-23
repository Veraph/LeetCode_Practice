class Solution {
public:
    vector<int> levelOrder(TreeNode *root) {
        if (!root) return {};
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        vector<int> res;

        while (!nodeQue.empty()) {
            TreeNode *cur = nodeQue.front(); nodeQue.pop();
            res.push_back(cur -> val);
            if (cur -> left) nodeQue.push(cur -> left);
            if (cur -> right) nodeQue.push(cur -> right);
        }
        return res;
    }
