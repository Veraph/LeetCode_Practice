# include <iostream>
# include <algorithm>
# include <vector>
using std::cin, std::cout, std::endl, std::min, std::max, std::vector;

int coinChange(vector<int> & coins, int target) {
    vector<int> dp(target + 1, INT_MIN);
    dp[0] = 0;
    for (int i = 1; i <= target; ++i) {
        for (int j = 0; j < coins.size(); ++j) {
            if (coins[j] <= i) {
                dp[i] = std::max(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }
    return dp[target];
}
    


int main() {
    int n; cin >> n;
    vector <int> coins(3);
    for (int i = 0; i < 3; ++i) {
        cin >> coins[i];
    }

    cout << coinChange(coins, n) << endl;
    return 0;
}

