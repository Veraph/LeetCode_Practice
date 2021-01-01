class Solution {
public:
    // two pointers
    vector<vector<int>> findContinuouSequence(int target) {
        int l = 1, r = 1;
        int sum = 0;
        vector<vector<int>> res;

        while (l <= (target >> 1)) {
            if (sum < target) {
                sum += r;
                r++;
            } else if (sum > target) {
                sum -= l;
                l++;
            } else {
                vector<int> tmp;
                for (int i = l; i < r; i++) {
                    tmp.push_back(i);
                }
                res.push_back(tmp);
                sum -= l;
                l++;
            }

        }
        return res;
    }
};
