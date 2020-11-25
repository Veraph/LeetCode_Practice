#include <iostream>
#include <numeric>
#include <algorithm>
#include <cmath>
using namespace::std;

const int maxN = 100000;
const long long init = 0;
long long nums[maxN];

int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> nums[i];
        }
        long long sum = accumulate(nums, nums + n, init);
        long long cnt = *max_element(nums, nums + n);
        cnt = max(cnt, (sum + n - 2) / (n - 1));

        cout << cnt * (n - 1) - sum << endl;
    }
    return 0;
}
