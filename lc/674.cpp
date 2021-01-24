class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int sz = nums.size();
        if (!sz) return 0;
        int pre = 1, cur = 1;
        for (int i = 1; i < sz; i++) {
            if (nums[i] > nums[i - 1]) {
                cur++;
            } else {
                pre = max(pre, cur);
                cur = 1;
            }
        }
        return max(cur, pre);
    }

};
