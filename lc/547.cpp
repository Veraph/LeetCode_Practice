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

// UnionFind
class UnionFind {
private:
    vector<int> parent;
public:

    UnionFind(int x) {
        parent.resize(x);
        iota(parent.begin(), parent.end(), 0);
    };

    // unite operation
    void unite(int x, int y) {
        parent[find(x)] = find(parent[y]);
    }

    // find operation
    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);   
        }
        return parent[x];
    }

    int retNum() {
        return set(parent.begin(), parent.end()).size();
    }
};


class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int sz = isConnected.size();
        UnionFind uf(sz);
        
        for (int i = 0; i < sz; i++) {
            for (int j = i + 1; j < sz; j++) {
                uf.unite(i, j);
            }
        }
        return uf.retNum();
    }
};
