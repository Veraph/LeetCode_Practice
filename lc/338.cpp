class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1);

        for (int i = 0; i <= num; i++) {
            res[i] = res[i >> 1] + (i & 1);
        }

        return res;
    }
};
