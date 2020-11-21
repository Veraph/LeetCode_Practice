#include <iostream>
#include <string>

using std::cin, std::cout, std::endl, std::string;

int main() {
    int T; cin >> T;
    while (T--) {
        int n, c, cc, h;
        cin >> n >> c >> cc >> h;
        string s; cin >> s;
        
        int num0 = 0;
        int num1 = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '0')
                num0++;
            else
                num1++;
        }
        
        int res = num0 * c + num1 * cc;
        
        int smallp, smalln, bigp, bign;
        if (c > cc) {
            smallp = cc;
            smalln = num1;
            bigp = c;
            bign = num0;
        } else if (c < cc) {
            smallp = c;
            smalln = num0;
            bigp = cc;
            bign = num1;
        } else {
            cout << res << endl;
            continue;
        }

        if (h >= (bigp - smallp)) {
            cout << res << endl;
        } else {
            res = n * smallp + bign * h;
            cout << res << endl;
        }
    }
    return 0;
}

