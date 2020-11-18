#include <iostream>
#include <string>
#include <cassert>

using namespace::std;

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long L, R; cin >> L >> R; R++;
        bool parity = 0;
        long long coef = 1;
        long long ans = 0;
        while (L < R) {
            auto is_good = [&](long long v) {
                bool d = v % 2;
                while (v > 0) {
                    if (v % 2 != d) return false;
                    d = !d;
                    v /= 10;
                }
                return d == 0;
            };
            while (L < R && L % 10 != 0) {
                if (is_good(L)) {
                    ans += coef;
                }
                L++;
            }
            while (L < R && R % 10 != 0) {
                --R;
                if (is_good(R)) {
                    ans += coef;
                }
            }

            if (L == R) break;

            L /= 10;
            R /= 10;

            coef *= 5;
            parity = !parity;
        }

        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

