class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        // pre deal with the matrix to let
        // the matrix[i][j] = all 1 on top of it (including itself)
        int m = matrix.size();
        int n = matrix[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0 && matrix[i][j])
                    matrix[i][j] += matrix[i - 1][j];
            }
        }

        // now every cell of the matrix can present all 1s on top of it
        // we could loop every cell to update the max area
        int res = 0;
        for (int i = 0; i < m; i++) {
            sort(matrix[i].begin(), matrix[i].end());
            for (int j = n - 1; j >= 0; j--) {
                res = max(res, matrix[i][j] * (n - j));
            }
        }

        return res;
    }
};
