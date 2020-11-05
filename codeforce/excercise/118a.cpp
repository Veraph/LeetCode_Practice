# include <iostream>
# include <string>
# include <algorithm>
# include <locale>

using std::cin, std::cout, std::string;

int main() {
    string s;
    cin >> s;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == 'A' || s[i] == 'a' || s[i] == 'E' || s[i] == 'e' || s[i] == 'O' || s[i] == 'o' || s[i] == 'Y' || s[i] == 'y' ||
            s[i] == 'U' || s[i] == 'u' || s[i] == 'I' || s[i] == 'i') {
            s.erase(i, 1);
            i--;
        } else {
            s[i] = std::tolower(s[i]);
            s.insert(i, ".");
            i++;
        }
    }
    cout << s << '\n';
    return 0;
}
