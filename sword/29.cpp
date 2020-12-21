class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        int len = matrix.size(), wid = len? matrix[0].size() : 0;
        int u = 0, d = len - 1, l = 0, r = wid - 1;
        int idx = 0;

        vector<int> res(len * wid);

        while (u <= d && l <= r) {
            // right direction loop
            for (int col = l; col <= r; col++) {
                res[idx++] = matrix[u][col];
            }
            if (++u > d) break;

            // down direction loop
            for (int row = u; row <= d; row++) {
                res[idx++] = matrix[row][r];
            }
            if (--r < l) break;

            // left direction loop
            for (int col = r; col >= l; col--) {
                res[idx++] = matrix[d][col];
            }
            if (--d < u) break;

            // up direction loop
            for (int row = d; row >= u; row--) {
                res[idx++] = matrix[row][l]; 
            }
            if (++l > r) break;
        }
        return res;
    }
};
