class Solution {
public:
    // brute force
    // TLE O(n^2)
    int reversePairs(vector<int>& nums) {
        if (nums.empty()) return 0;
        int res = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) 
                if (nums[i] > nums[j]) res++;
        }
        return res;
    }

    // merge sort
    // time O(nlogn)
    int reversePairs(vector<int>& nums) {
        int sz = nums.size();
        if (sz < 2) return 0;

        // initialize a new vector as the main vector
        vector<int> copy(sz);
        for (int i = 0; i < sz; i++) {
            copy[i] = nums[i];
        }

        // intialize an aux vector to help us do the merge sort
        vector<int> aux(sz);

        return reversePairs(copy, 0, sz - 1, aux);
    }

    int reversePairs(vector<int>& nums, int left, int right, vector<int>& aux) {
        if (left == right) return 0;

        int mid = left + ((right - left) >> 1);
        int leftPart = reversePairs(nums, left, mid, aux);
        int rightPart = reversePairs(nums, mid + 1, right, aux);

        if (nums[mid] <= nums[mid + 1]) return leftPart + rightPart;

        int crossPart = mergeAndSort(nums, left, mid, right, aux);
        return leftPart + rightPart + crossPart;
    }

    int mergeAndSort(vector<int>& nums, int left, int mid, int right, vector<int>& aux) {
        for (int i = left; i <= right; i++) {
            aux[i] = nums[i];
        }

        int i = left, j = mid + 1;
        int cnt = 0;
        for (int k = left; k <= right; k++) {
            if (i == mid + 1) {
                nums[k] = aux[j++];
            } else if (j == right + 1) {
                nums[k] = aux[i++];
            } else if (aux[i] <= aux[j]) {
                nums[k] = aux[i++];
            } else {
                nums[k] = aux[j++];
                cnt += (mid - i + 1);
            }

        }
        return cnt;
    }
};
