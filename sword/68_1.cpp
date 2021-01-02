class Solution {
public:
    // self-written
    // record path 
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> aux1;
        vector<TreeNode*> aux2;

        TreeNode* auxNode = root;
        while (auxNode != p) {
            if (havePath(auxNode -> left, p)) {
                aux1.push_back(auxNode -> left);
                auxNode = auxNode -> left;
            } else {
                aux1.push_back(auxNode -> right);
                auxNode = auxNode -> right;
            }
        }

        auxNode = root;
        while (auxNode != q) {
            if (havePath(auxNode -> left, q)) {
                aux2.push_back(auxNode -> left);
                auxNode = auxNode -> left;
            } else {
                aux2.push_back(auxNode -> right);
                auxNode = auxNode -> right;
            }
        }

        int i = 0, j = 0;
        TreeNode* ans = nullptr;
        while (i < aux1.size() && j < aux2.size()) {
            if (aux1[i] == aux2[j]) ans = aux1[i];
            i++;
            j++;
        }
        return ans;
    }

    bool havePath(TreeNode* node, TreeNode* target) {
        if (!node) return false;
        if (node == target) return true;
        return havePath(node -> right, target) || havePath(node -> left, target);
    }


    
    // dfs post order
    // time O(n) space O(n)
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || root == p || root == q) return root;
        // postorder
        TreeNode* left = lowestCommonAncestor(root -> left, p, q);
        TreeNode* right = lowestCommonAncestor(root -> right, p, q);
        if (!left) return right;
        if (!right) return left;
        return root;
    }
};
