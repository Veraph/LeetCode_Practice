class Solution {
public:
    // dfs    
    int findCircleNum(vector<vector<int>>& isConnected) {
        int sz = isConnected.size();
        vector<bool> visited(sz, false);
        int res = 0;
        for (int i = 0; i < sz; i++) {
            if (!visited[i]) {
                dfs(visited, i, isConnected);
                res++;
            }
        }
        return res;
    }

    void dfs(vector<bool>& visited, int idx, vector<vector<int>>& isConnected) {
        for (int i = 0; i < isConnected.size(); i++) {
            if (!visited[i] && isConnected[idx][i] == 1) {
                visited[i] = true;
                dfs(visited, i, isConnected);
            }
        }
    }
};

