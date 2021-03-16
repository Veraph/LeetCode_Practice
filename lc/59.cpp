class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int> (n));

        int idx = 1;
        int l = 0, r = n - 1, u = 0, d = n - 1;

        while (true) {
            for (int i = l; i <= r; i++) res[u][i] = idx++; 
            if (++u > d) break;

            for (int i = u; i <= d; i++) res[i][r] = idx++;
            if (--r < l) break;

            for (int i = r; i >= l; i--) res[d][i] = idx++;
            if (--d < u) break;

            for (int i = d; i >= u; i--) res[i][l] = idx++;
            if (++l > r) break;
        }

        return res;

    }
};
