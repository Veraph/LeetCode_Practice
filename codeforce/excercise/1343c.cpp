# include <iostream>
# include <algorithm>

using std::cin, std::cout, std::endl;

int main() {
    int t; cin >> t;
    for (int i = 0; i < t; ++i) {
        int n; cin >> n;
        long long nums[200000];
        cin >> nums[0];
        long long ans = 0, curr_max = nums[0];
        for (int i = 1; i < n; ++i) {
            cin >> nums[i];
            if (nums[i] * nums[i - 1] > 0) {
                curr_max = std::max(curr_max, nums[i]);
            } else {
                ans += curr_max;
                curr_max = nums[i];
            }
        }
        cout << ans + curr_max << endl;
    }
    return 0;
}


