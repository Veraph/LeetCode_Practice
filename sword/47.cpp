class Solution {
public:
    // dp
    // space O(m * n) or O(1)
    int maxValue(vector<vector<int>>& grid) {
        int m = grid[0].size(), n = grid.size();
        for (int i = 1; i < m; i++) {
            grid[0][i] += grid[0][i - 1];
        }

        for (int i = 1; i < n; i++) {
            grid[i][0] += grid[i - 1][0];
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[n - 1][m - 1];
    }

    // dp
    // space O(n)
    int maxValue(vector<vector<int>>& grid) {
        int m = grid[0].size(), n = grid.size();
        vector<int> aux(m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int left = 0, up = 0;
                if (i > 0) up = aux[j]; 
                if (j > 0) left = aux[j - 1];

                aux[j] = max(up, left) + grid[i][j];
            }
        }
        return aux[m - 1];
    }
};
