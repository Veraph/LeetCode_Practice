class UnionFind {
private:
    vector<int> parent;
public:

    UnionFind (int x) {
        parent.resize(x + 1);
        iota(parent.begin(), parent.end(), 0);
    };

    // union operation
    void unite(int x, int y) {
        parent[find(x)] = find(y);
    }


    // find operation
    int find(int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);
        return parent[x];
    }
};
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int sz = edges.size();
        UnionFind uf(sz);
        for (int i = 0; i < sz; i++) {
            if (uf.find(edges[i][0]) == uf.find(edges[i][1])) {
                // simple return
                // or we can use stack to store all these sets
                return edges[i];
            }
            uf.unite(edges[i][0], edges[i][1]);
        }
        return {};
    }
};

