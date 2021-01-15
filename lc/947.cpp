class UnionFind {
private:
    unordered_map <int, int> parent;

public:
    UnionFind() {
    };

    int count = 0;

    int find(int x) {
        if (!parent.count(x)) {
            parent[x] = x;
            count++;
        }

        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }



    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
            count--;
        }
    }
};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        UnionFind uf;
        int sz = stones.size();
        for (int i = 0; i < sz; i++) {
            uf.unite(stones[i][0] + 10001, stones[i][1]);
        }
        return sz - uf.count;
    }
};
