// DFS
class Solution {
public:

    int movingCount(int m, int n, int k) {
        vector<vector<bool>> flag(m, vector<bool>(n, 0));
        return dfs(0, 0, m, n, k, flag);
    }
private:
    int getDigit(int d) {
        int sum = 0;
        while (d > 0) {
            sum += d % 10;
            d /= 10;
        }
        return sum;
    }

    int dfs(int i, int j, int m, int n, int k, vector<vector<bool>> &flag) {
        if (i >= m || j >= n || k < getDigit(i) + getDigit(j) || flag[i][j])
            return 0;
        flag[i][j] = true;
        return 1 + dfs(i + 1, j, m, n, k, flag) + dfs(i, j + 1, m, n, k, flag);
    }

};

// BFS simulate with queue
class Solution {
    public:
        int getDigit(int n) {
            int sum = 0;
            while (n > 0) {
                sum += n % 10;
                n /= 10;
            }
            return sum;
        }
        int movingCount(int m, int n, int k) {
            vector<vector<bool>> flag(m, vector<bool>(n, 0));
            int res = 0;
            queue<vector<int>> que;
            que.push({0, 0});
            while (que.size() > 0) {
                vector<int> cur = que.front();
                que.pop();
                if (cur[0] >= m || cur[1] >= n || k < getDigit(cur[0]) + getDigit(cur[1]) || flag[i][j])
                    continue;
                res++;
                flag[cur[0]][cur[1]] = true;
                que.push({cur[0] + 1, cur[1]});
                que.push({cur[0], cur[1] + 1});
            }
            return res;
        }
};

// Iterate
class Solution {
    public:
        int getDigit(int n) {
            int sum = 0;
            while (n > 0) {
                sum += n % 10;
                n /= 10;
            }
            return sum;
        }

        int movingCount(int m, int n, int k) {
            if (!k) return 1;
            
            vector<vector<int>> flag(m, vector<int>(n, 0));
            flag[0][0] = 1;
            int res = 1;

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if ((i == 0 && j == 0) || k < getDigit(i) +  getDigit(j))
                        continue;

                    if (i > 0)
                        flag[i][j] |= flag[i - 1][j];
                    if (j > 0)
                        flag[i][j] |= flag[i][j - 1];
                    res += flag[i][j];
                }
            }
            return res;
        }
};









































