#include <iostream>
#include <string>

using namespace::std;
bool check(long long n) {
    unsigned len = std::to_string(n).length();

    int sign = (len % 2) ? 1 : 0;
    while (n) {
        if (n % 2 != sign) {
            return false;
        } else {
            sign = sign ^ 0x1;
            n /= 10;
        }
    }
    return true;
}

int main() {
    int T; cin >> T;
    for (int t = 0; t < T; ++t) {
        long long L, R;
        cin >> L >> R;
        long long res = 0;
        long long remain = L;
        while (L <= R) {
            if (check(L)) {
                res++;
                break;
            }
            L++;
        }
        if (R - L >= 20) {
            res += (R - L) / 20 * 5;
            remain = ((R - L) / 20) * 20 + L + 1;
        }
        for (long long i = remain; i <= R; ++i) {
            if (check(i))
                res++;
        }
        cout << "Case #" << t + 1 << ": " << res << endl;
    }
    return 0;
}

