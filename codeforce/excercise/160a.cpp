# include <iostream>
# include <numeric>
# include <algorithm>

using std::cin, std::cout;

int main() {
    int n;
    cin >> n;
    int vals[n];
    for (int i = 0; i < n; ++i) {
        cin >> vals[i];
    }
    int target = std::accumulate(vals, vals + n, 0) / 2;
    std::sort(vals, vals + n, [](int a, int b) {
            return a > b;
    });

    int curr = 0;
    for (int i = 0; i < n; ++i) {
        if (curr + vals[i] > target) {
            cout << (i + 1) << '\n';
            return 0;
        } else curr += vals[i];
    }
}

