class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sz = nums.size();
        int res = 0;
        for (int i = 0; i < k; i++) {
            res += nums[i];
        }
        
        int pre = res;
        int l = 0, r = k;
        while (r < sz) {
            pre = pre - nums[l] + nums[r];
            res = max(res, pre);
            l++; r++;
        }
        return (float) res / k;
        
    }
};
