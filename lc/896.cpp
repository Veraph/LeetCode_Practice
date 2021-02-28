class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int sz = A.size();
        bool inc = true, dec = true;

        for (int i = 0; i < sz - 1; i++) {
            if (A[i + 1] > A[i]) inc = false;

            if (A[i + 1] < A[i]) dec = false;
        }

        return inc || dec;
    }
};
