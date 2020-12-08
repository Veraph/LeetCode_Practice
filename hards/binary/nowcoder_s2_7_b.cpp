#include<iostream>

using namespace::std;

class Solution {

    int solve(string x) {
        auto check = [&] (int mid) {
            int cnt = 0, now = 0;
            for (char c : x) {
                if (c - 'a' == now)
                    cnt++;
                if (cnt == mid) {
                    cnt = 0;
                    now++;
                }
            }
            return now >= 3;
        };

        int l = 1, r = x.size() / 3, ans = 0, mid;
        while (l <= r) {
            mid = (l + r) >> 1;
            if (check(mid)) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans * 3;
    }
};
