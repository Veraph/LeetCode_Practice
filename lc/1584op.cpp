// use BIT(binary indexed tree) to optimize the
// original solving method (kruskal + unionfind)
// hit: there are three big part in total
// 1. UnionFind part which help to find the wheather two points is already connected
// 2. BIT part which help to maintain the points we will selected based on the main part
// 3. main part which do the UnionFind and BIT construction based on the edges picked (not all which will be O(n^2));


// the UnionFind part
class UnionFind {
private:
    vector<int> parent;
    vector<int> rank; // used to record the height of tree
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }

    // the find method
    int find(int x) {
        return x == parent[x] ? x : (parent[x] = find(parent[x]));
    }

    // the unite method
    bool unite(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return false;
        
        // do the combination based on rank
        if (rank[rootX] > rank[rootY]) swap(rootX, rootY);
        parent[rootX] = rootY;
        rank[rootY] += rank[rootX];
        return true;
    }
};

// the BIT part
class BIT {
private:
    vector<int> tree;
    vector<int> idRec;
    int n;
public:
    BIT(int _n) {
        n = _n;
        // why?
        tree.resize(n, INT_MAX);
        // why?
        idRec.resize(n, -1);
    }

    // the lowbit func
    int lowbit(int k) {
        return k & (-k);
    }

    // the update function
    // from the pos element
    // continually update the BIT tree
    // normally from small one to its ancestor
    // but there do the opposite
    // why?
    void update(int pos, int val, int id) {
        while (pos > 0) {
            if (tree[pos] > val) {
                tree[pos] = val;
                idRec[pos] = id;
            }
            pos -= lowbit(pos);
        }
    }

    // the query function
    // from the pos element
    int query(int pos) {
        int minVal = INT_MAX;
        int j = -1;
        while (pos < n) {
            if (minVal > tree[pos]) {
                minVal = tree[pos];
                // j means the jth point in the points?
                j = idRec[pos];
            }
            pos += lowbit(pos);
        }
        return j;
    }
};


// the aux structure
struct Edge {
    int len, x, y;
    Edge(int len, int x, int y): len(len), x(x), y(y) {}

    // reload the <
    bool operator < (const Edge& a) const { return len < a.len; }
};

struct Pos {
    int id, x, y;
    bool operator < (const Pos& a) const { return x == a.x ? y < a.y : x < a.x; }
};

// the main code part
class Solution {
public:
    vector<Edge> edges;
    vector<Pos> pos;

    // the main function
    int minCostConnectPoints(vector<vector<int>>& points) {
        int sz = points.size();
        solve(points, sz);

        UnionFind uf(sz);
        sort(edges.begin(), edges.end());
        int res = 0, num = 1;
        for (auto & [len, x, y] : edges) {
            if (uf.unite(x, y)) {
                res += len;
                num++;
                
                if (num == sz) break;
            }
        }
        return res;
    }

    // the aux functions
    // the solve function
    void solve(vector<vector<int>>& points, int sz) {
        // which helps to convert different part of points
        // into the p1 area
        pos.resize(sz);
        // (x, y)
        for (int i = 0; i < sz; i++) {
            pos[i].x = points[i][0];
            pos[i].y = points[i][1];
            pos[i].id = i;
        }
        build(sz);
        
        // (x, y) -> (y, x)
        for (int i = 0; i < sz; i++) {
            swap(pos[i].x, pos[i].y);
        }
        build(sz);

        // (y, x) -> (-y, x)
        for (int i = 0; i < sz; i++) {
            pos[i].x = -pos[i].x;
        }
        build(sz);

        // (-y, x) -> (x, -y)
        for (int i = 0; i < sz; i++) {
            swap(pos[i].x, pos[i].y);
        }
        build(sz);
    }

    // the build function
    void build(int sz) {
        // do all the building stuffs related to the BIT
        
        // 1. sort the pos to go from left -- top first
        sort(pos.begin(), pos.end());

        vector<int> a(sz), b(sz);
        for (int i = 0; i < sz; i++) {
            a[i] = pos[i].y - pos[i].x;
            b[i] = pos[i].y - pos[i].x;
        }

        // 2. remove the duplicate values
        sort(b.begin(), b.end()); // must sort first as unique only works when duplicates are near each other
        b.erase(unique(b.begin(), b.end()), b.end()); // this will delete the values from the last val not duplicate + 1 to the end

        // 3. construct the BIT based on the number of unique values
        int szB = b.size();
        BIT bit(szB + 1);
        for (int i = sz - 1; i >= 0; i--) {
            // why?
            // the lower_bound return an iterator point to the first val in the range that are not less than a[i]
            // and the poss hence calculate the distance between the val and the begin of b
            int poss = lower_bound(b.begin(), b.end(), a[i]) - b.begin() + 1;
            int j = bit.query(poss);
            if (j != -1) {
                int dis = abs(pos[i].x - pos[j].x) + abs(pos[i].y - pos[j].y);
                edges.emplace_back(dis, pos[i].id, pos[j].id);
            }
            // every time we got a new poss and done an query, we should update our BIT
            // why?
            bit.update(poss, pos[i].x + pos[i].y, i);

        }

    }
};
