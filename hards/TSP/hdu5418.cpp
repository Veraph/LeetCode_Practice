#include <iostream>
#include <cstring>
#include <vector>
#include <climits>
#include <algorithm>
using namespace::std;
const int INF = 0x3f3f3f3f;

const int maxN = 16;
int map[maxN][maxN];
int dp[(1 << 16)][maxN];

int main() {
    int T; cin >> T;
    while (T--) {
        memset(dp, INF, sizeof(dp));
        memset(map, INF, sizeof(map));
        int u, v, w, n, m;
        cin >> n >> m;
        // init the map matrix
        for (int i = 0; i < m; ++i) {
            cin >> u >> v >> w;
            --u; --v;
            map[u][v] = min(map[u][v], w);
            map[v][u] = min(map[v][u], w);
        }

        for (int i = 0; i < n; i++) {
            map[i][i] = 0;
        }

        // use floyd to cal the distance
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    map[i][j] = min(map[i][j], map[i][k] + map[k][j]);
                }
            }
        }

        // start case
        dp[0][0] = 0;
        // start dp
        for (int i = 0; i < (1 << n); ++i) {
            // loop every city as start point
            for (int j = 0; j < n; ++j) {
                if (dp[i][j] != INF) {
                    // current point
                    for (int k = 0; k < n; ++k) {
                        dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + map[j][k]);
                    }
                }
            }
        }

        cout << dp[(1 << n) - 1][0] << endl;

    }
    return 0;
}
                
    
