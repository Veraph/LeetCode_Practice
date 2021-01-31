// Time Complexity O(n^2 * m + nlogn)


class UnionFind {
private:
    vector<int> parent;
    vector<int> rank;
public:
    int Cnt;
    UnionFind(int n) {
        Cnt = n;
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        rank.resize(n, 1);
    }

    int find(int x) {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }

    void unite(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return;

        if (rank[rootX] > rank[rootY]) swap(rootX, rootY);
        parent[rootX] = rootY;
        rank[rootY] += rank[rootX];
        Cnt--;
    }
};

class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {
        // 1. build the UnionFind
        int sz = strs.size();
        UnionFind uf(sz);

        // 2. loop to construct the UnionFind
        for (int i = 0; i < sz; i++) {
            for (int j = i + 1; j < sz; j++) {
                if (isSimilar(strs[i], strs[j]))
                    uf.unite(i, j);
            }
        }

        // 3. return the ans;
        return uf.Cnt;
    }

    bool isSimilar(const string a, const string b) {
        int sz = a.size();
        int cnt = 0;
        for (int i = 0; i < sz; i++) {
            if (a[i] != b[i]) cnt++;
        }
        return cnt <= 2;
    }
};
