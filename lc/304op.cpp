class NumMatrix {
public:
    vector<vector<int>> aux;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m) {
            int n = matrix[0].size();
            aux.resize(m + 1, vector<int> (n + 1));

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    aux[i + 1][j + 1] = aux[i][j + 1] + aux[i + 1][j] - aux[i][j] + matrix[i][j];
                }
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return aux[row2 + 1][col2 + 1] - aux[row2 + 1][col1] - aux[row1][col2 + 1] + aux[row1][col1];
    }
};
