class Solution {
public:
    // print the results in a vector
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

    // print the results line by line
    vector<vector<int>> levelOrder(TreeNode *root) {
        if (!root) return {};
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        vector<vector<int>> res;

        while (!nodeQue.empty()) {
            int sz = nodeQue.size();
            vector<int> tmp(sz);
            while (sz--) {
                TreeNode *cur = nodeQue.front(); nodeQue.pop();
                tmp.push_back(cur -> val);
                if (cur -> left) nodeQue.push(cur -> left);
                if (cur -> right) nodeQue.push(cur -> right);
            }
            res.push_back(tmp);
        }
        return res;
    }

    // print the results line by line with z shape
    vector<vector<int>> levelOrder(TreeNode *root) {
        if (!root) return {};
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        vector<vector<int>> res;
        bool odd = 0;

        while (!nodeQue.empty()) {
            int sz = nodeQue.size();
            vector<int>tmp(sz);
            while (sz--) {
                TreeNode *cur = nodeQue.front(); nodeQue.pop();
                tmp[odd ? sz : tmp.size() - sz - 1] = cur -> val;
                if (cur -> left) nodeQue.push(cur -> left);
                if (cur -> right) nodeQue.push(cur -> right);
            }
            odd ^= 1;
            res.push_back(tmp);
        }
        return res;
    }
};
    }
