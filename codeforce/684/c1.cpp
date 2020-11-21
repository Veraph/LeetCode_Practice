#include <iostream>
#include <string>
using namespace::std;

const int MAX = 100;
int mat[MAX][MAX];
int sol[3*MAX*MAX][6];

int main() {
    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        string k;
        for (int i = 0; i < n; ++i) {
            getline(cin, k);
            for (int j = 0; j < m; ++j) {
                mat[i][j] = k[j] == '0' ? 0 : 1;
            }

        }
    return 0;
}

        
