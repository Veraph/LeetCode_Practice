class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int cols = matrix[0].size();
        int rows = matrix.size();

        vector<vector<int>> res (cols, vector<int> (rows);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                res[j][i] = matrix[i][j];
            }
        }

        return res;
    }
};
