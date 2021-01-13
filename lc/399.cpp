class UnionFind {
private:
    vector<int> parent;
    vector<double> weight;
public:
    // constructor
    UnionFind(int x) {
        parent.resize(x);
        iota(parent.begin(), parent.end(), 0);
        weight.resize(x);
        for (int i = 0; i < x; i++) {
            weight[i] = 1.0;
        }
    };

    // union operation
    void unite(int x, int y, double value) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) return;
        parent[rootX] = rootY;
        weight[rootX] = weight[y] * value / weight[x];
    }

    // find operation
    int find(int x) {
        if (x == parent[x])
            return x;
        int origin = parent[x];
        parent[x] = find(parent[x]);
        weight[x] *= weight[origin];
        return parent[x];
    }

    // isConnected operation
    double isConnected(int x, int y) {
        // if they have the same parent
        if (find(x) == find(y)) {
            return weight[x] / weight[y];
        }
        return -1.0;
    }
};




class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, 
            vector<vector<string>>& queries) {
        // initialize data structure
        int equaSZ = equations.size();
        UnionFind uf(2 * equaSZ);
        map<string, int> aux;
        int id = 0;
        // union operation
        for (int i = 0; i < equaSZ; i++) {
            string a = equations[i][0];
            string b = equations[i][1];
            if (aux.count(a) == 0) {
                aux[a] = id++;
            }

            if (aux.count(b) == 0) {
                aux[b] = id++;
            }
            if (a == NULL || b == NULL) continue;
            uf.unite(aux[a], aux[b], values[i]);
        }

        // find operation
        int querSZ = queries.size();
        vector<double> res(querSZ);
        for (int i = 0; i < querSZ; i++) {
            string a = queries[i][0];
            string b = queries[i][1];
            if (aux.count(a) == 0 || aux.count(b) == 0) {
                res[i] = -1.0;
                continue;
            }
            res[i] = uf.isConnected(aux[a], aux[b]);
        }
        return res;
    }
};
