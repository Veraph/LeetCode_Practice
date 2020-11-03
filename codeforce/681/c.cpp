# include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        long long a[n];
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        long long b[n];
        for (int i = 0; i < n; ++i)
            cin >> b[i];

        long long max_a = 0, accu_b = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] <= accu_b + b[i]) {
                max_a = max(max_a, a[i]);
            } else {
                accu_b += b[i];
            }
        }

        cout << max(max_a, accu_b) << endl;
    }
    return 0;
}