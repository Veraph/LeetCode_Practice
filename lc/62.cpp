// the dp problem
// look at how to optimize the space from O(m * n) to O(n)

class Solution {
public:
    // method1
    // space O(m*n)
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp (m, vector<int> (n));

        for (int i = 0; i < n; i++) {
            dp[0][i] = 1;
        }
        for (int j = 0; j < m; j++) {
            dp[j][0] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }

    // method2
    // space O(n)
    int uniquePaths2(int m, int n) {
        vector<int> dp (n, 1);
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
};
