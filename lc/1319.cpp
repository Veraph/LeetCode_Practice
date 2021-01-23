class UnionFind {
private:
    vector<int> parent;
    vector<int> size;
public:
    int setCnt;
    UnionFind(int n) {
        setCnt = n;
        parent.resize(n);
        size.resize(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }

    // find function
    int find(int x) {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }

    // unite function
    void unite(int x, int y) {
        int rootX = find(x), rootY = find(y);

        if (rootX == rootY) {
            return;
        }
        
        if (size[rootX] > size[rootY]) swap(rootX, rootY); 
        parent[rootX] = rootY;
        size[rootY] += size[rootX];
        setCnt--;
    }

};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        int sz = connections.size();
        // impossible situation
        if (sz + 1 < n) return -1;

        // do the union
        UnionFind uf(n);
        for (const auto &pair : connections) {
            uf.unite(pair[0], pair[1]);
        }

        return uf.setCnt - 1;
    }
};
