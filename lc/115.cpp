class Solution {
public:
    int numDistinct(string s, string t) {
        // 1. edge case
        int szS = s.size(), szT = t.size();
        if (szS < szT) return 0;

        // 2. normal case
        int res = 0;
        dfs(s, t, 0, 0, res);
        return res;

    }

    void dfs(string s, string t, int sIdx, int tIdx, int& cur) {
        // exit condition
        if (s.size() - sIdx < t.size() - tIdx) return;

        // meet condition
        if (tIdx == t.size()) {
            cur++;
            return;
        }

        // main loop
        for (int i = sIdx; i < s.size(); i++) {
            if (s[i] == t[tIdx]) dfs(s, t, i + 1, tIdx + 1, cur);
        }
    }

};
