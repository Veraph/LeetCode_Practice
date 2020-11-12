// Find num in two-dimensional array
# include <iostream>
# include <vector>
using std::vector;

bool func(vector<vector<int>> &matrix, int target) {

    int rows = matrix.size();
    if (rows == 0) return false;
    int cols = matrix[0].size();

    int row = 0, col = cols - 1;
    while (row < rows && col >= 0) {
        if (matrix[row][col] == target)
            return true;
        else if (matrix[row][col] > target)
            col--;
        else
            row++;
    }
    return false;
}


