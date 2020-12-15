// recursive
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return isSymmetric(root, root);
    }
    
    bool isSymmetric(TreeNode* root1, TreeNode* root2) {
        if (!root1 && !root2)
            return true;
        // this condition should be before the third one
        // or will arise nullptr error
        if (!root1 || !root2)
            return false;

        if (root1.val != root2.val)
            return false;

        return isSymmetric(root1 -> left, root2 -> right)
            && isSymmetric(root1 -> right, root2 -> left);
    }
};

// iteration

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;

        queue<TreeNode*> nodeQue;
        nodeQue.push(root -> left);
        nodeQue.push(root -> right);
        while (!nodeQue.empty()) {
            TreeNode *left = nodeQue.front(); nodeQue.pop();
            TreeNode *right = nodeQue.front(); nodeQue.pop();

            if (!left && !right) continue;

            if (!left || !right || left -> val != right -> val)
                return false;

            nodeQue.push(left -> left);
            nodeQue.push(right -> right);
            nodeQue.push(left -> right);
            nodeQue.push(right -> left);
        }
        return true;
    }
};
