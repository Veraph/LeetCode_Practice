// dp without space optimize
class Solution {
    int maxProfit1(vector<int> &prices, int fee) {
        int sz = prices.size();
        vector<vector<int>> dp(sz, vector<int> (2));
        dp[0][0] = 0; dp[0][1] = -prices[0];
        for (int i = 1; i < sz; i++) {
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee);
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }
        return dp[sz - 1][0];
    }
};

// dp with space optimization
class Solution {
    int maxProfit2(vector<int> &prices, int fee) {
        int sz = prices.size();
        vector<int> dp(2);
        dp[0] = 0, dp[1] = -prices[0];
        for (int i = 0; i < sz; i++) {
            int temp = dp[0];
            dp[0] = max(dp[0], dp[1] + prices[i] - fee);
            dp[1] = max(dp[1], temp - prices[i]);
        }
        return dp[0];
    }
};

// greedy
class Solution {
public:
    int maxProfit3(vector<int> &prices, int fee) {
       int profit = 0;
       int minPrice = prices[0];

       for (int i = 1; i < prices.size(); i++) {
           // really sell and but a new one
           if (prices[i] < minPrice) minPrice = prices[i];

           // continually gain, not really sell
           // add up the profit of every single day
           if (prices[i] > minPrice + fee) {
               profit += prices[i] - minPrice - fee;
               minPrice = prices[i] - fee;
           }
       }
       return profit;
    }
};
