# include <iostream>
# include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        long long max_a = 0, accu_b = 0;
        long long a[n];
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        long long b[n];
        for (int i = 0; i < n; ++i) {
            cin >> b[i];
            accu_b += b[i];
        }
            
        long long ans = LLONG_MAX;
        sort(a, a + n);
        sort(b, b + n);
        for (int i = 0; i < n; ++i) {
            ans = min(ans, max(max_a, accu_b));
            max_a = max(max_a, a[i]);
            accu_b -= b[i];
            ans = min(ans, max(max_a, accu_b));
        }
        cout << ans << endl;
    }
    return 0;
}
