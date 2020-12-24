class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    vector<vector<int>> pathSum(TreeNode *root, int sum) {
       dfs(root, sum);
       return res;
    }
    
    void dfs(TreeNode *root, int tar) {
        if (!root) return;

        tar -= root -> val;
        path.push_back(root -> val);

        if (!root -> left && !root -> right && !tar)
            res.push_back(path);

        dfs(root -> left, tar);
        dfs(root -> right, tar);
        // the parameters are references (&)
        // remember to remove it!
        path.pop_back();
    }
};
