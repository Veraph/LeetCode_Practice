class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int cols = A[0].size();
        int rows = A.size();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (j < cols / 2) swap(A[i][j], A[i][cols - 1 - j]);
                A[i][j] ^= 1;
            }
        }
        return A;

    }
};
