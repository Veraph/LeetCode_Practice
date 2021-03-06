class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int sz = nums.size();
        vector<int> res (sz, -1);
        stack<int> aux;

        for (int i = 0; i < sz * 2 - 1; i++) {
            while (!aux.empty() && nums[aux.top()] < nums[i % sz]) {
                res[aux.top()] = nums[i % sz];
                aux.pop();
            }
            aux.push(i % sz);
        }

        return res;
    }
};
