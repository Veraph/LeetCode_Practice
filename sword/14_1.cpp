class Solution {
public:
    const long long MOD = 1e9 + 7;
    int cuttingRope(int n) {
	if (n == 2) {
            return 1;
	}
	if (n == 3) {
	    return 2;
	}

	int cnt3 = n / 3;
	if (n % 3 == 1) {
	    cnt3--;
        }
        
        int cnt2 = (n - cnt3 * 3) / 2;

        long long res = 1;
        for (int i = 0; i < cnt2; ++i) {
            res *= 2;
            res %= MOD;
        }
        for (int j = 0; j < cnt3; ++j) {
            res *= 3;
            res %= MOD;
        }
        return res;
    }
};
