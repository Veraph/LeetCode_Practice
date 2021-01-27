class UnionFind {
private:
    vector<int> aParent;
    vector<int> bParent;
public:
    int aCnt, bCnt, can;
    UnionFind(int n) {
        can = 0;
        aCnt = n;
        bCnt = n;
        aParent.resize(n + 1); iota(aParent.begin(), aParent.end(), 0);
        bParent.resize(n + 1); iota(bParent.begin(), bParent.end(), 0);
    }

    int find(vector<int>& parent, int x) {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }

    void unite(int idx, int x, int y) {
        if (idx == 1) {
            int rootX = find(aParent, x);
            int rootY = find(aParent, y);
            if (rootX == rootY) {
               can++;
               return;
            }
            aparent[rootX] = rootY;
            aCnt--;
        } else if (idx == 2) {
            int rootX = find(bParent, x);
            int rootY = find(bParent, y);
            if (rootX == rootY) {
                can++;
                return;
            }
            bparent[rootX] = rootY;
            bCnt--;
        } else {
            int rootX = find(aParent, x);
            int rootY = find(aParent, y);
            if (rootX == rootY) {
                can++;
                rootX = find(bParent, x);
                rootY = find(bParent, y);
                return;
            }
            aParent[rootX] = rootY; aCnt--;
            rootX = find(bParent, x);
            rootY = find(bParent, y);
            bParent[rootX] = rootY; bCnt--;
        }

    }

};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        // 1. sort the edges to let type 3 edges first
        sort(edges.begin(), edges.end(), [] (auto & a, auto & b) -> int { return a[0] > b[0];});

        // 2. construct the unionfind
        UnionFind uf(n);
        for (auto & group : edges) {
            uf.unite(group[0], group[1], group[2]);
        }

        // 3. cal the connected number and return
        int allCnt = uf.aCnt + uf.bCnt;
        if (allCnt == 2) return uf.can;
        else return -1;
    }
};
