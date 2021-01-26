class Solution {
public:
    int numEquiv(vector<vector<int>>& dominoes) {
        vector<int> freq(100);
        int res = 0;
        for (auto & item : dominoes) {
            int val = item[0] > item[1] ? item[0] * 10 + item[1] : item[1] * 10 + item[0];
            res += freq[val]++;
        }
        return res;
    }

}
