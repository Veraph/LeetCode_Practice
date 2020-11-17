#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace::std;

bool common(string a, string b) {
    for (int i = 0; i < a.size(); ++i) {
        for (int j = 0; j < b.size(); ++j) {
            if (a[i] == b[j])
                return true;
        }
    }
    return false;
}

int main() {
    int T; cin >>T;
    string a[50001];
    a[0] = " ";
    for (int t = 0; t < T; ++t) {
        int N, Q; cin >> N >> Q;
        for (int n = 1; n <= N; ++n) {
            cin >> a[n];
        }
        for (int q = 0; q < Q; ++q) {
            int s, e;
            cin >> s >> e;
            int cnt = 2;
            if (common(a[s], a[e])) {
                cout << cnt << endl;
            } else {
                cnt++;
                for (int i = 1; i <= N; ++i) {
                    if (i != s && i != e) {   
                        if (common(a[s], a[i])
                                if (common(a[i], a[e])
                                    cout << cnt << endl;
                    }
                }
            }
            cout << -1 << endl;
        }
    }
    return 0;
}

