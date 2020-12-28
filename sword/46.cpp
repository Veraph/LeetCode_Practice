class Solution {
public:
    // dp
    // time o(n) space O(n)
    int translateNum(int num) {
        string sNum = to_string(num);
        vector<int> dp(sNum.size());
        int cnt = 0;
        for (int i = sNum.size() - 1; i >= 0; i--) {
            if (i < sNum.size() - 1) cnt = dp[i + 1];
            else cnt = 1;

            if (i < sNum.size() - 1) {
                int digit1 = sNum[i] - '0', digit2 = sNum[i + 1] - '0';
                int cur = digit1 * 10 + digit2;
                if (cur >= 10 && cur <= 25) {
                    if (i < sNum.size() - 2) cnt += dp[i + 2];
                    else cnt++;
                }
            }

            dp[i] = cnt;
        }
        return dp[0];
    }

    // dp with optimization
    // space O(1)
    int translateNum(int num) {
        string sNum = to_string(num);
        int pre = 1, cur = 1;
        for (int i = 2; i <= sNum.size(); i++) {
            string tmp = sNum.substr(i - 2, 2);
            int cnt = tmp >= "10" && tmp <= "25" ? cur + pre : cur;
            pre = cur;
            cur = cnt;
        }
        return cur;
    }

    // recursion
    // time O(2^n), space O(n)
    int translateNum(int num) {
        string sNum = to_string(num);
        return backTrack(sNum, 0);
    }

    int backTrack(string& s, int idx) {
        int sz = s.size();
        if (sz == idx) return 1;
        if (idx == sz - 1 || s[idx] == '0' || s.substr(idx, 2) > "25") 
            return backTrack(s, idx + 1);
        return backTrack(s, idx + 1) + backTrack(s, idx + 2);
    }
};
