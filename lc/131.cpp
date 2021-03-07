class Solution {
private:
    vector<vector<string>> res;
    bool check(string s) {
        int sz = s.size();
        for (int i = 0; i < sz / 2; i++) {
            if (s[i] != s[sz - 1 - i]) return false;
        }
        return true;
    }

    void dfs(string s, int idx, vector<string> vec) {
        if (idx > s.size() - 1) {
            res.emplace_back(vec);
            return;
        }

        for (int i = 0; i < s.size() - idx; i++) {
            if (check(s.substr(idx, idx + i) {
                
            }

        }

    }


public:
    vector<vector<string>> partition(string s) {


    }

}
