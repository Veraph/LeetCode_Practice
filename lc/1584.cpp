class UnionFind {
private:
    vector<int> father;
    vector<int> rank;
public:
    UnionFind(int n) {
        father.resize(n);
        rank.resize(n, 1);
        iota(father.begin(), father.end(), 0);
    }

    int find(int x) {
        return x == father[x] ? x : find(father[x]);
    }

    bool unite(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return false;
        father[rootX] = rootY;
        rank[rootY] += rank[rootX];
        return true;
    }

};

struct Edge {
    int dist, x, y;
    Edge(int dist, int x, int y) : dist(dist), x(x), y(y) {}
};



class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        // a function to calculate manhaton dist
        auto dist = [&](int x, int y) -> int {
            return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1]);
        };
        
        // initialize data structures
        // including edge len vector and the union find set
        int sz = points.size();
        vector<Edge> edge;
        UnionFind uf(sz);
        for (int i = 0; i < sz; i++) {
            for (int j = 1; j < sz; j++) {
                edge.emplace_back(dist(i, j), i, j);
            }
        }
        
        // sort the edge based on the distances
        sort(edge.begin(), edge.end(), [](Edge a, Edge b) -> int {return a.len < b.len;});

        // do the union and find
        int res = 0, cnt = 0;
        for (auto & [dist, x, y] : edge) {
            if (unite(x, y)) {
                res += len;
                cnt++;
                if (cnt == sz) break;
            }
        }
        return res;

    }

};
