class Solution {
public:
    const int MOD = 1e9 + 7;
    int concatenatedBinary(int n) {
        long long ans = 0;
        int shift = 0;
        // the equation is
        // x = x << shift + i
        for (int i = 1; i <= n; ++i) {
            // every time we arrived in the power pf 2
            // we increase the shift
            if (!(i & (i - 1))) {
                ++shift;
            }
            ans = ((ans << shift) + i) % MOD; 
        }
        return (int) ans;
    }
};

        
