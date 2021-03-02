class NumMatrix {
public:
    vector<vector<int>> aux;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (!m) return;

        int n = matrix[0].size();
        aux.resize(m, vector<int> (n + 1));

        for (int i = 0; i < m; i++) {
            aux[i][0] = 0;
            aux[i][1] = matrix[i][0];
        }

        for (int i = 0; i < m; i++) {
            for (int j = 2; j < n; j++) {
                aux[i][j] = aux[i][j - 1] + matrix[i][j - 1];
            }
        }

    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int res = 0;
        for (int i = row1; i <= row2; i++) {
            res += (aux[i][col2 + 1] - aux[i][col1]);
        }
        return res;
    }
};
