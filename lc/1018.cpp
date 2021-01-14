class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& A) {
        vector<bool> res;
        int sz = A.size();
        int val = 0;
        for (int i = 0; i < sz; i++) {
            val = (val << 1) + A[i];
            val %= 5;
            if (val % 5 == 0) res.push_back(true);
            else res.push_back(false);
        }
        return res;
    }
};
