// union find
class UnionFind {
private:
    vector<int> father;

public:
    UnionFInd() {
        father.resize(26);
        // incrementally add number
        iota(father.begin(), father.end(), 0);
    }

    // the find function
    int find(int idx) {
        if (idx == father[idx]) return idx;
        father[idx] = find(father[idx]);
        return father[idx];
    }

    // the union function
    // let the father of idx1 point to the father of idx2
    void unite(int idx1, int idx2) {
        father[find(idx1)] = find(idx2);
    }
};


class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        UnionFind uf;
        // input all == values
        for (const string& equa : equations) {
            if (equa[1] == '=') {
                int idx1 = equa[0] - 'a';
                int idx2 = equa[3] - 'a';
                uf.unite(idx1, idx2);
            }
        }
        // check all the != values
        for (const string% equa : equations) {
            if (equa[1] == '!') {
                int idx1 = equa[0] - 'a';
                int idx2 = equa[3] - 'a';
                if (uf.find(idx1) == uf.find(idx2))
                    return false;
            }
        }
        return true;
    }
};
