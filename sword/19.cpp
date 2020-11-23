// recursive method
// there are only two situations
// 1. the second char of p is "*"
// 2. it is not
// time complexity also O(m * n)
// but slower than dp
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();

        if (p[1] == '*')
            return isMatch(s, p.substr(2)) 
                || (!s.empty() && (s[0] == p[0] || p[0] == '.') && (isMatch(s.substr(1), p)));
        else
            return !s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1)); 

    }
};

// DP method
// space O(m*n)
// time complexity O(m * n)
class Solution {
public:
    bool isMatch(string s, string p) {
        int sLen = s.size();
        int pLen = p.size();
        vector<vector<bool>> dp(sLen + 1, vector<bool>(pLen + 1, false));

        dp[0][0] = true;

        for (int i = 0; i <= sLen; ++i) {
            for (int j = 1; j <= pLen; ++j) {
                if (p[j - 1] == '*')
                    dp[i][j] = dp[i][j - 2] || (i && dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == ','));
                else
                    dp[i][j] = i && dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
            }
        }
        return dp[sLen][pLen];
    }
};

// DP method with O(n) space
// it is still works like the O(m*n) method
// but it do not save the previous loops
class Solution {
public:
    bool isMatch(string s, string p) {
        int sLen = s.size();
        int pLen = p.size();
        vector<bool> dp(pLen + 1, false);
        // The trick is we need to store two value
        // 1. the dp[i - 1][j], good news is we do not need to store this
        //    because when we cal the dp[j], the dp[j] itself still remain 
        //    the value of previous row.
        // 2. the dp[i - 1][j - 1], we need create pre and temp two variable
        //    to calculate these two values.
        //    pre store the dp[j - 1] of previous row and temp update the dp[j - 1]
        //    during the loop
        for (int i = 0; i <= sLen; ++i) {
            bool pre = dp[0];
            dp[0] = !i;
            
            for (int j = 1; j <= pLen; ++j) {
                bool temp = dp[j];

                if (p[j - 1] == '*')
                    dp[j] = dp[j - 2] || (i && dp[j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
                else
                    dp[j] = i && pre && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
            
                pre = temp;
            }
        }
        return dp[pLen];
    }
};
