#include <iostream>
#include <cstring>
#include <vector>
#include <climits>
#include <algorithm>
using namespace::std;

// initialize map
const int maxN = 16;
int map[maxN][maxN];
//vector<vector<int>> map (maxN, vector<int> (maxN, INT_MAX));

// initialize dp
const int M = (1 << maxN);
int dp[M][maxN];
//vector<vector<int>> dp (maxN, vector<int> (M, INT_MAX));

int main() {
    memset(map, INT_MAX, sizeof(map));
    memset(dp, INT_MAX, sizeof(dp));
    int T; cin >> T;
    while (T--) {
        // for every test cases, there are n cities and m lines
        int n, m; cin >> n >> m;
        // read the costs
        for (int i = 0; i < m; i++) {
            int ui, vi, wi; cin >> ui >> vi >> wi;
            map[ui - 1][vi - 1] = min(map[ui - 1][vi - 1], wi);
        }
        
        // start dp
        for (int m = 0; m < M; m++) {
            // loop start point
            for (int i = 0; i < n; i++)
                // ensure the jth is in the set
                if (m & (1 << i)) {
                    // loop through current city
                    for (int j = 0; j < n; j++) {
                        if (!(m & (1 << j)) && (map[i][j] != INT_MAX))
                            // the value in current city equals to the min
                            // between the current one and the prev one plus the edge
                            dp[j][m | (1 << j)] = min(dp[j][m | (1 << j)], dp[i][m] + map[i][j]); 
                    }
                }
        }

        // add back the city
        int ans = INT_MAX;
        for (int i = 0; i < n; i++) {
            ans = min(ans, dp[M][i] + map[i][0]);
        }
        cout << ans << endl;
    }
    return 0;
}
