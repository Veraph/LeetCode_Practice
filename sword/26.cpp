// Recursion
class Solution {
public:
    const double fact = 1e-8;

    bool isSubStructure(TreeNode *A, TreeNode *B) {
        bool res = false;

        // robutness
        if (A && B) {
            if (A -> val == B -> val) {
                res = help(A, B);
            }
            if (!res)
                res = isSubStructure(A -> left, B);
            if (!res)
                res = isSubStructure(A -> right, B);
        }
        return res;
    }

    bool help(TreeNode *A, TreeNode *B) {
        if (!B) return true;
        if (!A) return false;

        if (A -> val != B -> val) return false;

        return help(A -> left, B -> left) && help(A -> right, B -> right);
    }
    
    bool equal(double x, double y) {
        if ((x - y > -fact) && (x - y < fact))
            return true;
        else
            return false;
    }
};

// Iteration using queue
// but still need recursion
// in the help function
class Solution {
public:
    bool isSubStructure(TreeNode *A, TreeNode *B) {
        if (!A || !B) return false;
        queue<TreeNode*> nodeA;
        nodeA.push(A);

        while (nodeA.size()) {
            TreeNode *cur = nodeA.front();
            nodeA.pop();
            if (cur -> val == B -> val)
                if help(cur, B) return true;
            if (cur -> left)
                nodeA.push(cur -> left);
            if (cur -> right)
                nodeA.push(cur -> right);
        }
        return false;
    }

    bool help(TreeNode *A, TreeNode *B) {
        if (!B) return true;
        if (!A) return false;

        if (A -> val != B -> val) return false;

        return help(A -> left, B -> left) && help(A -> right, B -> right);
    }

};
