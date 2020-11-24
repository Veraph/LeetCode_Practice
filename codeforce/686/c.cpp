#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace::std;

int solve(vector<int> nums, int idx) {
    int block = 1;
    int tar = nums[idx];
    bool ready = false;
    for (int i = idx + 1; i < nums.size(); i++) {
        if (nums[i] == tar && !ready)
            continue;
        else if (nums[i] != tar)
            ready = true;

        if (ready && nums[i] == tar) {
            block++;
            ready = false;
        }
    }
    block++;
    if (nums[0] == tar) {
        block--;
    }
    if (nums[nums.size() - 1] == tar) {
        block--;
    }
    return block;
}


int main() {
    int t; cin >> t;
    while (t--) {
        map<int, int> visited;
        int n; cin >> n;
        vector<int> nums(n);
        for (int i = 0; i < n; ++i) {
            cin >> nums[i];
        }
        int res = 200001;
        for (int i = 0; i < n; ++i) {
            if (visited[nums[i]]) {
                continue;
            } else {
                visited[nums[i]]++;
                res = min(res, solve(nums, i));
            }
        }
        cout << res << endl;
    }
    return 0;
}


