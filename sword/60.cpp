class Solution {
public:
    // dp
    vector<double> dicesProbability(int n) {
        vector<vector<int>> dp(12, vector<int> (75, 0));

        // initialize border case
        for (int i = 1; i <= 6; i++) {
            dp[1][i] = 1;
        }

        // main loop
        // loop for dices
        for (int i = 2; i <= n; i++) {
            // loop for different numbers we could get
            for (int j = i; j <= 6 * i; j++) {
                // loop for current point of dices
                for (int cur = 1; cur <= 6; cur++) {
                    if (j < cur) break;
                    dp[i][j] += dp[i - 1][j - cur];
                }
            }
        }

        // calculate the probabilities
        int all = pow(6, n);
        vector<double> res;
        for (int i = n; i <= 6 * n; i++) {
            res.push_back(dp[n][i] * 1.0 / all);
        }
        return res;
    }

    // dp optimize
    vector<double> dicesProbability(int n) {
        vector<int> dp(75, 0);
        
        for (int i = 1; i <= 6; i++) {
            dp[i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            // we have to reverse if we use 1d array
            for (int j = i * 6; j >= i; j--) {
                dp[j] = 0; // very important to avoid duplicated adding
                for (int cur = 1; cur <= 6; cur++) {
                    // the minimum points we could get if we have i - 1 dices are i
                    if (j - cur < i - 1) break;
                    dp[j] += dp[j - cur];
                }
            }
        }
        int all = pow(6, n);
        vector<double> res;
        for (int i = n; i <= 6 * n; i++) {
            res.push_back(dp[i] * 1.0 / all);
        }
        return res;
    }
};
