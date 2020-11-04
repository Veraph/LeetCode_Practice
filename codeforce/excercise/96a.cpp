# include <iostream>
# include <algorithm>
# include <string>

using std::cin, std::cout, std::string;

int main() {
    string s;
    cin >> s;
    int cnt = 1;
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] == s[i - 1]) {
            cnt += 1;
            if (cnt > 6) {
                cout << "YES" << '\n';
                return 0;
            }
        } else cnt = 1;
    }
    cout << "NO" << '\n';
    return 0;
}

