class NumArray {
public:
    
    vector<int> sums;

    NumArray(vector<int>& nums) {
        // calculate the pre sum
        int sz = nums.size();
        sums.resize(sz + 1);
        sums[0] = 0;
        for (int i = 0; i < sz; i++) {
            sums[i + 1] = nums[i] + sums[i];
        }
    }

    int sumRange(int i, int j) {
        return sums[j + 1] - sums[i];
    }

};
