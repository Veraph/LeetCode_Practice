// a.cpp Array Rearrangement

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x; cin >> n >> x;
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        int b[n];
        for (int i = 0; i < n; i++)
            cin >> b[i];
        bool flag = 1;
        for (int i = 0; i < n; ++i) {
            if (a[i] + b[n - 1 - i] > x) {
                flag = 0;
                break;
            }
        }
        cout << (flag ? "Yes" : "No") << endl;
    }
}
