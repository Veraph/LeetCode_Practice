class Solution {
public:
    // brute force, level loop and reverse odd levels
    vector<vector<int>> zigzagLevelOrder1(TreeNode *root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        int level = 0;
        while (!nodeQue.empty()) {
            vector<int> tmpVec;
            int sz = nodeQue.size();
            while (sz--) {
                TreeNode *cur = nodeQue.front(); nodeQue.pop();
                tmpVec.push_back(cur -> val);
                if (cur -> left) nodeQue.push(cur -> left);
                if (cur -> right) nodeQue.push(cur -> right);
            }
            if (level++ & 1) reverse(tmpVec.begin(). tmpVec.end());
            res.push_back(tmpVec);
        }
        return res;
    }

    // prefered one, manually order
    // since we already know the size of each level
    vector<vector<int>> zigzagLevelOrder2(TreeNode *root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        int level = 0;
        bool odd = 0;
        while (!nodeQue.empty()) {
            int sz = nodeQue.size();
            vector<int> tmpVec(sz); int tmpVecSz = tmpVec.size();
            while (sz--) {
                TreeNode *cur = nodeQue.front(); nodeQue.pop();
                tmpVec[odd? sz : tmpVecSz - sz - 1] = cur -> val;
                if (cur -> left) nodeQue.push(cur -> left);
                if (cur -> right) nodeQue.push(cur -> right);
            }
            odd ^= 1;
            res.push_back(tmpVec);
        }
        return res;
    }
};
