#include <cmath>   // pow()

// O(1) greedy
class Solution {
public:
    int cuttingRope(int n) {
        if (n == 2)
            return 1;
        if (n == 3)
            return 2;

        int cnt3 = n / 3;
        if (n - cnt3 * 3 == 1)
            cnt3--;

        int cnt2 = (n - cnt3 * 3) / 2;

        return pow(2, cnt2) * pow(3, cnt3);
    }
};


// O(n) greedy and dp
class Solution {
public:
    int cuttingRope(int n) {
    
        if (n == 2)
            return 1;
        if (n == 3)
            return 2;

        long long cut[59];
        cut[2] = 2;
        cut[3] = 3;
        cut[4] = 4;
        for (int i = 5; i <= n; i++) {
            cut[i] = cut[3] * cut[i - 3];
        }
        return cut[n];
    }
};
