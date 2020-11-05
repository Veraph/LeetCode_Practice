# include <iostream>

using std::cin, std::cout;
int main() {
    // use the greedy
    int n;
    cin >> n;
    int cnt[5] = {0, 0, 0, 0, 0};
    int val;
    for (int i = 0; i < n; ++i) {
        cin >> val;
        cnt[val]++;
    }
    int ans = 0;
    // all 4
    ans += cnt[4];
    cnt[4] = 0;

    // for 3 and 1 pair
    while (cnt[3] && cnt[1]) {
        ans += 1;
        cnt[3]--;
        cnt[1]--;
    }

    // for 2 and 2 pair
    while (cnt[2] > 1) {
        ans += 1;
        cnt[2] -= 2;
    }

    // for 2 and 1 pair
    while (cnt[2] && cnt[1] > 1) {
        ans += 1;
        cnt[2] --;
        cnt[1] -= 2;
    }

    // for single 2 and 1
    while (cnt[2] && cnt[1]) {
        ans++;
        cnt[2]--;
        cnt[1]--;
    }

    // deal with remaining one
    if (cnt[2])
        ans += 1;

    if (cnt[1]) {
        if (cnt[1] >= 4) {
            ans += cnt[1] / 4;
            cnt[1] %= 4;
        }
        if (cnt[1])
            ans += 1;
    }

    if (cnt[3])
        ans += cnt[3];

    cout << ans << '\n';

    return 0;
}
