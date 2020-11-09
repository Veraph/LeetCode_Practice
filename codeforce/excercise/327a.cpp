# include <iostream>
# include <algorithm>

using std::cin, std::cout, std::endl;

int main() {
    int n;
    cin >> n;
    int board[100];
    int dp[100];
    int oneNum = 0;
    int x;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x == 1) {
            oneNum++;
            board[i] = -1;
        } else
            board[i] = 1;
    }
    dp[0] = board[0];
    
    for (int i = 1; i < n; ++i) {
        dp[i] = std::max(dp[i - 1] + board[i], board[i]);
    }

    cout << *std::max_element(dp, dp + n) + oneNum << endl;
    return 0;
}

    
