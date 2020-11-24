#include <iostream>
#include <algorithm>

using namespace::std;

int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int nums[n];
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        sort(nums, nums + n, greater<int>());
        if (n % 2 == 1) {
            int temp = nums[n / 2];
            nums[n / 2] = nums[n - 1];
            nums[n - 1] = temp;
        }
        for (int i = 0; i < n; i++) {
            cout << nums[i] << ' ';
        }
        cout << endl;
    }
    return 0;
}
