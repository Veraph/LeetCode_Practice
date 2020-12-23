class Solution {
public:
    // use a aux stack to simulate the operation
    bool validateStackSequences(vector<int> &pushed, vector<int> &popped) {
        stack<int> aux;
        int i = 0;
        for (int n : pushed) {
            aux.push(n);
            while (!aux.empty() && aux.top() == popped[i]) {
                aux.pop();
                i++;
            }
        }
        return aux.empty();
    }
};
