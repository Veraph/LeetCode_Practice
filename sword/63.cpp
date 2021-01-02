class Solution {
public:
    // dp
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0, minPrice = INT_MAX;
        for (int i : prices) {
            minPrice = min(minPrice, i);
            maxProfit = max(i - minPrice, maxProfit);
        }
        return maxProfit;
    }
};
