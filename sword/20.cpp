#include <iostream>
#include <string>
using namespace::std;

class Solution {
private:
    bool scanInteger(const string s, int &idx) {
        if (s[idx] == '+' || s[idx] == '-') {
            idx++;
        }
        return scanUnsignedInteger(s, idx);
    }

    bool scanUnsignedInteger(const string s, int &idx) {
        const int pre = idx;
        while (idx < s.size() && s[idx] >= '0' && s[idx] <= '9')
            idx++;

        return idx > pre;
    }

public:
    bool isNumber(string s) {
        
        int idx = 0;
        // the previous blank is accepted
        while (s[idx] == ' ')
            idx++;

        bool numeric = scanInteger(s, idx);

        // when we meet '.'
        if (s[idx] == '.') {
            idx++;
            // the order is important
            // because if the numeric is true
            // it will not gointo the scanUnsignedInteger function
            numeric = scanUnsignedInteger(s, idx) || numeric;
        }

        // when we meet 'e' or 'E'
        if (s[idx] == 'e' || s[idx] == 'E') {
            idx++;
            numeric = numeric && scanInteger(s, idx);
        }

        // deal with the blanks in the tails
        while (s[idx] == ' ')
            idx++;
        
        return numeric && (idx == s.size());
    }
};

int main() {
    Solution s1;
    string a = "0.8";
    bool res = s1.isNumber(a);
    cout << res << endl;

    return 0;
}
