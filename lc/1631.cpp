class Solution {
public:
    int res = INT_MAX;
    int rows, cols;
    vector<vector<int>> DIRECTIONS {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    int minimumEffortPath(vector<vector<int>>& heights) {
        rows = heights.size();
        cols = heights[0].size();

        dfs(heights, 0, 0, INT_MIN);
        return res;
    }

    // dfs function
    void dfs(vector<vector<int>>& heights, int i, int j, int cur) {
        // exit condition
        if (cur > res) return;
        if (i == rows - 1 && j == cols - 1) {
            res = min(cur, res);
            return;
        }

        // loop condition
        for (auto & dir : DIRECTIONS) {
            int newI = i + dir[0];
            int newJ = j + dir[1];
            if (newI < 0 || newJ < 0 || newI > rows - 1 || newJ > cols - 1) continue;
            if (heights[newI][newJ] == -1) continue;
            int tmp = heights[newI][newJ];
            heights[newI][newJ] = -1;
            cur = max(cur, abs(heights[i][j] - heights[newI][newJ]);
            dfs(heights, newI, newJ, cur);
            heights[newI][newJ] = tmp;
        }
    
    }

};
