class Solution {
public:
    // brute force
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        for (int i = 0; i < nums.size() - k + 1; i++) {
            int numMax = INT_MIN;
            for (int j = i; j < i + k; j++) {
                numMax = max(numMax, nums[j]);
            }
            res.push_back(numMax);
        }
        return res;
    }
    // deque (double ended queue)
    vector<int> maxSlidingWindow(vector<int>& nums. int k) {
        if (nums.empty()) return {};

        vector<int> res;
        deque<int> aux;

        for (int i = 0; i < k; i++) {
            while (!aux.empty() && nums[i] >= nums[aux.back()])
                aux.pop_back();
            aux.push_back(i);
        }

        for (int i = k; i < nums.size(); i++) {
            res.push_back(nums[aux.front()]);

            while (!aux.empty() && nums[i] >= nums[aux.back()])
                aux.pop_back();
            if (!aux.empty() && aux.front() <= (i - k))
                aux.pop_front();

            aux.push_back(i);
        }
        res.push_back(nums[aux.front()]);
        return res;
    }
};
