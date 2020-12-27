class Solution {
public:
    // sort(), O(n(logn))
    vector<int> getLeastNumbers(vector<int> &arr, int k) {
        sort(arr.begin(), arr.end());
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(arr[i]);
        }
        return res;
    }

    // heap
    // time O(nlogk); space O(k)
    vector<int> getLeastNumbers(vector<int> &arr, int k) {
        if (!k || arr.empty()) return {};
        
        vector<int> res (k, 0);
        priority_queue<int> kQue;
        for (int i = 0; i < k; i++) {
            kQue.push(arr[i]);
        }

        for (int i = k; i < arr.size(); i++) {
            if (kQue.top() > arr[i]) {
                kQue.pop();
                kQue.push(arr[i]);
            }
        }

        for (int i = 0; i < k; i++) {
            res[i] = kQue.top();
            kQue.pop();
        }
        return res;

    }

    // quick select  partition
    // time O(n)
    vector<int> getLeastNumbers(vector<int> &arr, int k) {
        if (!k || arr.empty()) return {};

        return quickSearch(arr, 0, arr.size() - 1, k - 1);
    }

    vector<int> quickSearch(vector<int> &nums, int l, int r, int k) {
        int j = partition(nums, l, r);

        if (j == k) return vector<int> (nums.begin(), nums.begin() + k + 1);

        return j > k? quickSearch(nums, l, j - 1, k) : quickSearch(nums, j + 1, r, k);
    }

    int partition(vector<int> &nums, int l, int r) {
        int pivot = nums[l];
        int i = l, j = r + 1;
        while (true) {
            while (++i <= r && nums[i] < pivot);
            while (--j >= l && nums[j] > pivot);
            if (i >= j) break;

            swap(nums[i], nums[j]);
        }
        swap(nums[l], nums[j]);
        return j;
    }
};
