# include <iostream>
# include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;
        string maps;
        cin >> maps;

        long long mine_len, mine_cnt, zero_cnt, begin_idx, end_idx;
        for (int i = 0; i < maps.length(); ++i) {
            if (maps[i] == '1') {
                mine_cnt = 1;
                begin_idx = i;
                for (int j = begin_idx; j < maps.length(); ++j) {
                    if (maps[j] == '1') {
                        mine_cnt ++;
                        end_idx = j;
                    }
                }
                break;
            }
            break;
        }
        mine_len = end_idx - begin_idx + 1;
        zero_cnt = mine_len - mine_cnt;
        long long ans;

        if (zero_cnt == 0) {
            ans = a;
        } else {
            if (a > b) {
                ans = zero_cnt * b + a;
            } else {
                ans = (zero_cnt + 1) * a;
            }
        }
        cout << ans << endl;
        return 0;
    }
}