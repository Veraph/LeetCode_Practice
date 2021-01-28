class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sz = nums.size();
        if (!sz) return -1;

        int after = 0, pre = 0;
        for (int num : nums) after += num;

        for (int i = 0; i < sz; i++) {
            after -= nums[i];
            if (pre == after) return i;
            pre += nums[i];
        }

        return -1;
    }
};
