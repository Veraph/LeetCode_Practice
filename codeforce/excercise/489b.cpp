# include <iostream>
# include <algorithm>
# include <stdlib.h>

using std::cin, std::cout, std::endl;

int main() {

    int boys[100];
    int girls[100];
    
    int n; cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> boys[i];
    
    int m; cin >> m;
    for (int i = 0; i < m; ++i)
        cin >> girls[i];

    // for every boy, loop the girl to
    // find the minimum one that fits
    // complexity o(mn)

    std::sort(boys, boys + n);
    std::sort(girls, girls + m);
    if ((boys[n - 1] < girls[0] - 1) || (boys[0] - 1 > girls[m - 1])) {
        cout << 0 << endl;
        return 0;
    }
    int ans = 0;
    int idx = 0;
    for (int b = 0; b < n; ++b) {
        for (int g = idx; g < m; ++g) {
            if (abs(boys[b] - girls[g]) <= 1) {
                ans++;
                idx = g + 1;
                break;
            }
        }
    }
    cout << ans << endl;
    return 0;
}
