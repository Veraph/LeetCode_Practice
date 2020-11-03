# include <iostream>
# include <algorithm>
# include <string>
using std::cin, std::cout, std::string;

int main() {
    int n;
    cin >> n;
    while (n--) {
        string s, ans; 
        cin >> s;
        if (s.size() > 10) {
            string num = std::to_string(s.size() - 2);
            ans += (s[0] + num + s[s.size() - 1]);
            cout << ans << '\n';
        } else 
            cout << s << '\n';
    }
    return 0;
}
