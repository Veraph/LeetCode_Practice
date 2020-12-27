class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = nums[0], cur = 0;
        int res = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            cur = max(nums[i], nums[i] + pre);
            pre = cur;
            res = max(cur, res);
        }
        return res;
    }
};
