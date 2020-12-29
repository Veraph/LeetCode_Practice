class Solution {
public:
    // binary search
    int missingNumber(vector<int> &nums) {
       int l = 0, r = nums.size() - 1;
       while (l <= r) {
            int m = l + ((r - l) >> 1);
            if (nums[m] == m) l = m + 1;
            else r = m - 1;
       }
       return l;
    }
};
