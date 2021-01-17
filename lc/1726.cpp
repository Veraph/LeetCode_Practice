// dfs will TLE
// think easily
// use a map to record all possible multiplies
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<int, int> freq;
        int sz = nums.size();
        for (int i = 0; i < sz; i++) {
            for (int j = i + 1; j < sz; j++) {
                freq[nums[i] * nums[j]]++;
            }
        }

        int res = 0;
        for (auto c : freq) {
            res += (c.second * (c.second - 1) >> 1);
        }
        return res * 8;
    }
};
