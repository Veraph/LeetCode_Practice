class Codec {
public:
    string serialize(TreeNode *root) {
        if (!root) return "";
        ostringstream out;
        queue<TreeNode*> nodeQue; nodeQue.push(root);
        while (!nodeQue.empty()) {
            TreeNode* tmp = nodeQue.front(); nodeQue.pop();
            if (tmp) {
                out << tmp -> val << " ";
                nodeQue.push(tmp -> left);
                nodeQue.push(tmp -> right);
            } else {
                out << "null ";
            }
        }
        return out.str();
    }
    
    // using vector to deserialize
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        istringstream input(data); string node;
        vector<TreeNode*> aux;
        while(input >> node) {
            if (node != "null")
                aux.push_back(new TreeNode(stoi(node)));
            else aux.push_back(NULL);
        }

        int idx = 1;
        for (int i = 0; idx < aux.size(); i++) {
            if (!aux[i]) continue;
            if (idx < aux.size()) aux[i] -> left = aux[idx++];
            if (idx < aux.size()) aux[i] -> right = aux[idx++];
        }

        return aux[0];
    }

    // using queue to deserialize
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        istringstream input(data); string node;
        input >> node;
        queue<TreeNode*> nodeQue; nodeQue.push(new TreeNode(stoi(node)));
        TreeNode *head = nodeQue.front();
        while (!nodeQue.empty()) {
            TreeNode *cur = nodeQue.front(); nodeQue.pop();
            input >> node;
            if (node != "null") {
                cur -> left = new TreeNode(stoi(node));
                nodeQue.push(cur -> left);
            }
            input >> node;
            if (node != "null") {
                cur -> right = new TreeNode(stoi(node));
                nodeQue.push(cur -> right);
            }
        }
        return head;
    }
};
