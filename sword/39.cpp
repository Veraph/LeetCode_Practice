class Solution {
public:
    // first O(n)  TLE!!!
    // partition
    int majorityElement(vector<int> &nums) {
        int mid = nums.size() >> 1;
        int start = 0, end = nums.size() - 1;
        int idx = partition(nums, start, end);
        while (idx != mid) {
            if (idx > mid) {
                end = idx - 1;
                idx = partition(nums, start, end);
            } else {
                start = idx + 1;
                idx = partition(nums, start, end);
            }
        }
        return nums[mid];
    }

    int partition(vector<int> &nums, int l, int r) {
        int pivot = nums[r], small = 0;
        for (int i = l; i < r; i++) {
            if (nums[i] <= pivot) swap(nums[small++], nums[i]);
        }
        swap(nums[small], nums[r]);
        return small;
    }
    // second o(n) and also space O(1);
    // property
    int majorityElement(vector<int> &nums) {
        if (nums.empty()) return 0;

        int freq = 1, res = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (!freq) {
                res = nums[i];
                freq = 1;
            } else if (nums[i] == res) freq++;
            else freq--;
        }
        return res;
    }

    // third O(n)
    // map
    int majorityElement(vector<int> &nums) {
        if (nums.empty()) return 0;
        map<int, int> freq;
        for (int i : nums) {
            if (++freq[i] > (nums.size() / 2)) return i;
        }
        return 0;
    }
};
