class UnionFind {
private:
    vector<int> parent;
    vector<int> size;
public:
    UnionFind(int n) {
        for (int i = 0; i < n; i++) {
            parent.push_back(i);
            size.push_back(1);
        }
    };

    // unite operation
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        }
    }

    // find operation
    int find(int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);
        return parent[x];
    }


    // return the size connected to the node
    int getSZ(int x) {
        return size(find(x));
    }
};

class Solution {
private:
    int rows, cols;
    vector<vector<int>> DIRECTIONS {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    int getIdx(int x, int y) {
        return x * cols + y;
    }

    bool legal(int x, int y) {
        return x >= 0 && y >= 0 && x < cols && y < rows;
    }

public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        // 1. clear all bricks will be clear
        rows = grid.size();
        cols = grid.size();
        // create a copy matrix
        vector<vector<int>> copy(rows, vector<int> (cols, 0));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                copy[i][j] = grid[i][j];
            }
        }
        // clear all hitten bricks in copy matrix
        for (vector<int> hit : hits) {
            copy[hit[0]][hit[1]] = 0;
        }


        // 2. build the map and construct Union Find
        int sz = rows * cols;
        UnionFind uf (sz + 1); // the additional one used to store the roof
        // firstly connect all roof node to the roof
        for (int j = 0; j < cols; j++) {
            if (copy[0][j])
                uf.unite(j, sz);
        }
        // then connect other nodes
        for (int i = 1; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (copy[i][j]) {
                    // for every bricks, check the bricks on the left and right
                    if (copy[i - 1][j])
                        uf.unite(getIdx(i - 1, j), getIdx(i, j));
                    if (j > 0 && copy[i][j - 1])
                        uf.unite(getIdx(i, j - 1), getIdx(i, j));
                }
            }
        }


        // 3. Feed back all hitten bricks and calculate the number missed
        int hitLen = hits.size();
        vector<int> res(hitLen);
        for (int i = hitLen - 1; i >= 0; i--) {
            int x = hits[i][0];
            int y = hits[i][1];

            if (!grid[x][y]) continue;
            
            // the origin number of bricks connect with roof
            int origin = uf.getSZ(sz);

            if (x == 0) uf.unite(y, sz);

            for (vector<int> dir : DIRECTIONS) {
                int newX = x + dir[0];
                int newY = y + dir[1];

                if (legal(newX, newY) && copy[newX][newY] == 1) {
                    uf.unite(getIdx(newX, newY), getIdx(x, y));
                }
            }

            // the current number of bricks
            int current = uf.getSZ(sz);
            copy[x][y] = 1;
            res[i] = max(0, current - origin - 1);
        }
        return res;
    }
};
