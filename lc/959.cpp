class UnionFind {
private:
    vector<int> parent;
public:
    int cnt;

    UnionFind(int n) {
        cnt = n;
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }

    void unite(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return;
        parent[rootX] = rootY;
        cnt--;
    }
};


class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int sz = grid.size();
        int N = 4 * sz * sz;
        
        UnionFind uf(N);
        for (int i = 0; i < sz; i++) {
            for (int j = 0; k < sz; j++) {
                int idx = 4 * (i * sz + j);
                if (grid[i][j] == '/') {
                    uf.unite(idx, idx + 3);
                    uf.unite(idx + 1, idx + 2);
                } else if (grid[i][j] == '\\') {
                    uf.unite(idx, idx + 1);
                    uf.unite(idx + 2, idx + 3);
                } else {
                    uf.unite(idx, idx + 1);
                    uf.unite(idx, idx + 2);
                    uf.unite(idx, idx + 3);
                }

                // combine bottom and right directions
                if (j + 1 < sz) {
                    uf.unite(idx + 1, 4 * (i * sz + j + 1) + 3);
                }

                if (i + 1 < sz) {
                    uf.unite(idx + 2, 4 * ((i + 1) * sz + j));
                }

            }
        }
        return uf.cnt;

    }
};
