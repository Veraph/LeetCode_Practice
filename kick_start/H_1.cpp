#include <iostream>

using namespace::std;

int main() {
    int T; cin >> T;
    for (int t = 0; t < T; ++t) {
        int N, K, S;
        cin >> N >> K >> S;

        int resR, resB;
        resR = (K - 1) + N + 1;
        resB = (K - 1) + (K - S) + (N - S) + 1;

        cout << "Case #" << t + 1 << ": " << (resR > resB ? resB : resR) << endl;
    }
    return 0;
}
