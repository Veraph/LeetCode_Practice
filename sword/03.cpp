// sort
class Solution {
public:
    int findRepeatNumber(vector<int> &nums) {
        sort(nums.begin(), nums.begin() + nums.size());
        return 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1]) {
                return nums[i];
            }
        }
        return -1;
    }
};

// map
class Solution {
public:
    int findRepeatNumber(vector<int> &nums) {
        map<int, int> freq;
        for (int i = 0; i < n; i++) {
            if (++freq[nums[i]] > 1) {
                return nums[i];
            }
        }
        return -1;
    }
};

// In array solving method
// !!if the number of range in (0, n - 1)
// in the n length arrary
// pretty fast
class Solution {
public:
    int findRepeatNumber(vector<int> &nums) {
        if (nums.size() < 2)
            return -1;
        for (int i = 0; i < nums.size(); i++) {
            while (nums[i] != i) {
                // if nums[i] appear once more in the 
                // place taht are not nums[nums[i]]
                if (nums[i] == nums[nums[i]]) {
                    return nums[i];
                }

                int temp = nums[i];
                nums[i] = nums[temp];
                nums[temp] = temp;
            }
        }
        return -1;
    }
};

// One more method that do not need
// us to edit the array
// using binary search
class Solution {
public:
    int findRepeatNumber(vector<int> &nums) {
        // special case we return -1
        if (nums.size() < 2) {
            return -1;
        }

        // binary search
        int start = 1;
        int end = nums.size() - 1;
        while (end >= start) {
            // optimize to get the round up val
            int mid = ((end - start) >> 1) + start;
            int cnt = cntRange(nums, start, mid);
            if (end == start) {
                if (cnt > 1) {
                    return start;
                } else {
                    break;
                }
            }

            if (cnt > (mid - start + 1))
                end = mid;
            else
                start = mid + 1;
        }
        return -1;
    }

    int cntRange(vector<int> &nums, int start, int end) {
        int cnt = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] >= start && nums[i] <= end)
                cnt++;
        }
        return cnt;
    }
};


// also can use two pointer 
// to find the entry point of a loop
class Solution {
public:
    int findRepeatNumber(vector<int> &nums) {

    }
};
