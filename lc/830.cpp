class Solution {
public:
    // O(n)
    vector<vector<int>> largeGroupPositions(string s) {
        if (s.empty()) return {};
        vector<vector<int>> res;
        int sz = s.size(), idx = 0, cnt = 0;
        while (idx < sz) {
            vector<int> tmp {idx};
            cnt = 1;
            int i = idx + 1;
            for (; i < sz; i++) {
                if (s[i] == s[idx]) cnt++;
                else break;
            }
            if (cnt >= 3) {
                tmp.push_back(i - 1);
                res.push_back(tmp);
            }
            idx = i;
        }
        return res;
    }

    // O(n)
    // optimize
    vector<vector<int>> largeGroupPositions(string s) {
        if (s.empty()) return {};
        int sz = s.size(), num = 1;
        vector<vector<int>> res;
        for (int i = 0; i < sz; i++) {
            if (i == sz - 1 || s[i] != s[i + 1]) {
                if (num >= 3)
                    res.push_back({i - num + 1, i});
                num = 1;
            } else num++;
        }
        return res;
    }
};
