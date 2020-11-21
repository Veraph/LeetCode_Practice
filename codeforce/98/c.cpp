#include <iostream>
#include <string>

using namespace::std;

int main() {
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        int res = 0;
        int l1 = 0, l2 = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                l1++;
            }
            if (s[i] == '[') {
                l2++;
            }
            if (s[i] == ')') {
                if (l1) {
                    l1--;
                    res++;
                }
            }
            if (s[i] == ']') {
                if (l2) {
                    l2--;
                    res++;
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}
