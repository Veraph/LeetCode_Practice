class Solution {
public:
    vector<int> exchange(vector<int> &nums) {
        vector<int> res(nums,size());
        int beg = 0;
        int end = nums.size() - 1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] & 0x1) {
                res[beg++] = nums[i];
            } else {
                res[end--] = nums[i];
            }
        }
        return res;
    }
};

// O(1) solution which do not need a res vector
// just two pointers
class Solution {
public:
    vector<int> exchange(vector<int> &nums) {
        int beg = 0;
        int end = nums.size() - 1;
        while (beg < end) {
            if (nums[beg] & 0x1) {
                beg++;
                continue;
            }
            if (!(nums[end] & 0x1)) {
                end--;
                continue;
            }
            int temp = nums[beg];
            nums[beg] = nums[end];
            nums[end] = temp;
            beg++;
            end--;
        }
        return nums;
    }
};

// Adaptable solving method
class Solution {
public:
    bool standard(int x) {
        return (x & 0x1);
    }

    vector<int> exchange(vector<int> & nums) {
        if (nums.size() == 0)
            return nums;

        int beg = 0;
        int end = nums.size() - 1;
        while (beg < end) {
            if (standard(nums[beg])) {
                beg++;
                continue;
            }
            if (!standard(nums[end])) {
                end--;
                continue;
            }
            int temp = nums[beg];
            nums[beg] = nums[end];
            nums[end] = temp;
        }
        return nums;
    }
};
