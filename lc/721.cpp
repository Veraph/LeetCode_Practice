class UnionFind {
private:
    vector<int> parent;

public:
    UnionFind(int x) {
        parent.resize(x);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY)
            parent[rootX] = rootY;
    }

};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        // 1.initialize UnionFind and construct emailToId map and do the merge
        int sz = accounts.size();
        UnionFind uf(sz);
        unordered_map<string, int> emailToId;
        for (int i = 0; i < sz; i++) {
            string base = accounts[i][1];
            for (int j = 1; j < accounts[i].size(); j++) {
                string e = accounts[i][j];
                if (!emailToId.count(e)) {
                    emailToId[e] = i;
                }
                uf.unite(emailToId[e], emailToId[base]);
            }
        }

        // 2. construct the idToEmail map and sort each id's email
        unordered_map<int, vector<string>> idToEmail;
        for (auto & [email, id] : emailToId) {
            idToEmail[uf.find(id)].push_back(move(email));
        }

        for (auto & [id, emails] : idToEmail) {
            sort(emails.rbegin(), emails.rend());
        }


        // 3. construct result and return it
        vector<vector<string>> res;
        for (auto & [id, emails] : idToEmail) {
            emails.push_back(accounts[id][0]);
            reverse(emails.begin(), emails.end());
            res.push_back(move(emails));
        }
        return res;
    }
};
