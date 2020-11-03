# include <iostream>
# include <string>
# include <algorithm>
# define ll long long
using std::cin, std::string, std::min, std::endl, std::cout;

int main() {
    int t;
    cin >> t;
    while (t--) {
        ll a, b;
        cin >> a >> b;
        string maps;
        cin >> maps;
        
        ll ans = a, i;
        // find the first 1
        for (i = 0; i < maps.size(); ++i) {
            if (maps[i] == '1')
                break;
        }
        
        ll len_0 = 0;
        if (i == maps.size()){
            cout << 0 << endl;
            continue;
        }

        // every time we meet 0 cout up
        // and when we meet 1, we calculate
        for (; i < maps.size(); ++i) {
            if (maps[i] == '0')
                len_0++;
            else {
                ans += min(len_0 * b, a);
                len_0 = 0;
            }
        } 
        cout << ans << endl;
    }
    return 0;
}
