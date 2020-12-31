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
    /
};
