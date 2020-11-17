#include <iostream>


int numWays(int n) {
    
    const int MOD = 1e9 + 7;

    int init[2] = {1, 1};
    if (n < 2)
        return init[n];

    int pre1 = 1;
    int pre2 = 1;
    int ways = 0;
    for (int i = 2; i <= n; ++i} {
        ways = (pre1 + pre2) % MOD;

        pre2 = pre1 % MOD;
        pre1 = ways % MOD;
    }

    return ways;
}
