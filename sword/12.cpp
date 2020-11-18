class Solution {
public:
        int m, n;

        bool dfs(vector<vector<char>>& board, string word, int idx, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || word[idx] != board[i][j]) return false;
        if (idx == word.size() - 1) return true;

        char cur = board[i][j];
        board[i][j] = '-';
        bool searchNext = dfs(board, word, idx + 1, i + 1, j)
                       || dfs(board, word, idx + 1, i - 1, j)
                       || dfs(board, word, idx + 1, i, j - 1)
                       || dfs(board, word, idx + 1, i, j + 1);
        board[i][j] = cur;
        return searchNext;
    }
   
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, 0, i, j))
                        return true;
                }
            }
        }
        return false;
    }
 
};
