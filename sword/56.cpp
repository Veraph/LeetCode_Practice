class Solution {
public:
    // bit operation
    vector<int> singleNumbers(vector<int>& nums) {
        int aux = 0;
        for (int i : nums) aux ^= i;

        int bit = 1;
        // find any bit that equals to 1
        while (!(bit & aux)) {
            bit <<= 1;
        }
        int res1 = 0, res2 = 0;
        for (int i : nums) {
            if (bit & i) res1 ^= i;
            else res2 ^= i;
        }
        return vector<int> {res1, res2};
    }

    // binary
    // actually slower O(nlogn)
    vector<int> singleNumbers(vector<int>& nums) {
        int minNum = INT_MAX, maxNum = INT_MIN, aux = 0;
        int cntZero = 0;
        for (int i : nums) {
            if (i == 0) cntZero++;
            
            aux ^= i;
            minNum = min(minNum, aux);
            maxNum = max(maxNum, aux);
        }
        
        // special case
        if (cntZero == 0)
            return vector<int> {aux, 0};


        // binary search
        int l = minNum, r = maxNum;
        while (l <= r) {
            int m = l + (r - l) / 2;
            int left = 0, right = 0;
            for (int i : nums) {
                if (m >= i) left ^= i;
                else right ^= i;
            }

            if (left && right) {
                return vector<int> {left, right};
            } else if (!left) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return {};
    }
};
