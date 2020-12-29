class Solution {
public:
    // two pointer seach
    // O(n)
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            if (nums[l] == target && nums[r] == target) return r + 1 - l;
            if (nums[l] != target) {
                l++;
            }
            if (nums[r] != target) {
                r--;
            }
        }
        return 0;
    }

    // binary search
    // O(logn)
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, target) - binarySearch(nums, target - 1);
    }

    int binarySearch(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int m = l + ((r - l) >> 1);
            if (nums[m] <= target) i = m + 1;
            else j = m - 1;
        }
        return i;
    }
    
};
