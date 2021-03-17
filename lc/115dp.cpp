class Solution {
public:
    int numDistinct(string s, string t) {
        int szS = s.size(), szT = t.size();
        if (szS < szT) return 0;

        vector<vector<long>> dp(szS + 1, vector<long> (szT + 1));
        for (int i = 0; i <= szS; i++) {
            dp[i][szT] = 1;
        }

        for (int i = szS - 1; i >= 0; i--) {
            for (int j = szT - 1; j >= 0; j--) {
                if (s[i] == t[j]) dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j];
                else dp[i][j] = dp[i + 1][j];

            }
        }
        return dp[0][0]; 

    }
};

