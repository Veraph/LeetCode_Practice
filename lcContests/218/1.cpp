#include <iostream>
using namespace::std;

const int MOD = 1000000007;
int main() {
    int n; cin >> n;
    int ans = 0;
    int shift = 0;
    int times = 0;
    for (int i = n; i > 0; i--) {
        ans += (i << shift);
        while (i != 0) {
            i >>= 1;
            times++;
        }
        shift += times;
    }
    cout << ans % MOD << endl;
}

