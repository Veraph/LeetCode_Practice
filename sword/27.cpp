// recursive
class Solution {
public:
    TreeNode* mirrorTree(TreeNode *root) {
        if (!root) return NULL;
        
        TreeNode *temp = root -> left;
        root -> left = mirrorTree(root -> right);
        root -> right = mirrorTree(temp);

        return root;
    }

};

// iterate
class Solution {
public:
    TreeNode* mirrorTree(TreeNode *root) {
        if (!root) return NULL;
        queue<TreeNode*> nodeQueue;
        nodeQueue.push(root);
        while (!nodeQueue.empty()) {
            // even we face a nullptr
            // we should also invert it
            TreeNode *node = nodeQueue.front();
            nodeQueue.pop();
            TreeNode *temp = node -> left;
            node -> left = node -> right;
            node -> right = temp;

            if (node -> left) nodeQueue.push(node -> left);
            if (node -> right) nodeQueue.push(node -> right);
        }
        return root;
    }
};
