// a.cpp - reorder

# include <iostream>
# include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            m -= x;
        }
        cout << (m == 0 ? "YES" : "NO") << endl;
    }
    return 0;
}