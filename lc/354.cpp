class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int sz = envelopes.size();
        if (!sz) return 0;

        // sort the envelopes
        sort(envelopes.begin(), envelopes.end(), [] (const auto& e1, const auto& e2) { return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]); });


        vector<int> dp = {envelopes[0][1]};
        for (int i = 0; i < sz; i++) {
            if (int num = envelopes[i][1]; num > dp.back()) dp.push_back(num);
            else {
                // find the first position that is not smaller than num
                // hence the position before will be smaller than num
                // the lower_bound func has complexity of O(nlogn) which 
                // is the binary search
                auto it = lower_bound(dp.begin(), dp.end(), num);
                *it = num;
            }
        }

        return dp.size();
    }
};
