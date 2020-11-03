# include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int cnt = 2 * n;
        for (int i = 0; i < n; ++i) {
            cout << cnt << " ";
            cnt += 2;
        }
        cout << endl;
    }
    return 0;
}