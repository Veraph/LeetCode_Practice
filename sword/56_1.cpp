class Solution {
public:
    // loop O(n)
    // space O(32) = O(1)
    int singleNumber(vector<int>& nums) {
        vector<int> aux(32, 0);
        for (int i : nums) {
            unsigned bitMask = 1;
            for (int j = 31; j >= 0; j--) {
                int bit = i & bitMask;
                if (bit) aux[j]++;
                bitMask <<= 1;
            }
        }

        int res = 0;
        for (int i : aux) {
            res <<= 1;
            res += i % 3;
        }
        return res;
    }


    // Finite State Automation
    int singleNumber(vector<int>& nums) {
        int one = 0, two = 0;
        for (int i : nums) {
            one = one ^ i & ~two;
            two = two ^ i & ~one;
        }
        // because we want the num that appear once
        // hence only return one
        return one;
    }
};
