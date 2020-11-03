// c.cpp Division
#include <iostream>
using namespace std;

int main () {
    int t;
    cin >> t;
    while (t--) {
        long long p, q;
        cin >> p >> q;
        long long f = p, s = q, x = 0;
        for (int i = 2; i * i <= q; ++i) {
            int cnt = 0;
            // which means q % i == 0
            while (!(q % i)) {
                q /= i;
                cnt++;
            }
            if (cnt) {
                p = f;
                while (!(p % s))
                    p /= i;
                x = max(x, p);
            }
        }
        if (q > 1) {
            p = f;
            while (!(p % s))
                p /= q;
            x = max(x, p);
        }
        cout << x << endl;
    }
    return 0;
}