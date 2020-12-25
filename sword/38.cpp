class Solution {
public:
    // backtracking algorithm
    vector<string> permutation(string s) {
        if (s.empty()) return {};
        // sort to let the same char next to each other
        sort(s.begin(). s.end());
        vector<string> res;
        vector<bool> visited(s.size(), false);
        string cur;
        
        backtrack(res, visited, s, cur);
        return res;
    }

    void backtrack(vector<string> &res, vector<bool> &visited, string s, string &cur) {
        if (s.size() == cur.size()) {
            res.push_back(cur);
            return;
        }

        for (int i = 0; i < s.size(); i++) {
            if (visited[i]) continue;
            if (i > 0 && !visited[i - 1] && s[i - 1] == s[i]) continue;
            visited[i] = true;

            cur.push_back(s[i]);
            backtrack(res, visited, s, cur);
            cur.pop_back();
            visited[i] = false;
        }
    }
    

    // swap and backtrack
    // slower
    vector<string> permutation(string s) {
        // use set to remove duplicative
        set<string> res;
        backtrack(s, 0, res);
        return vector<string> (res.begin(), res.end());
    }

    void backtrack(string s, int idx, set<string> &res) {
        if (idx == s.size()) {
            res.insert(s);
            return;
        }

        for (int i = idx; i < s.size(); i++) {
            swap(s[i], s[start]);
            backtrack(s, idx + 1, res);
            // cancel the swap
            swap(s[start], s[i]);
        }
    }

};
