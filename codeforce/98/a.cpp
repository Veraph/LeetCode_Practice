#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace::std;

int main() {
    int t; cin >> t;
    while (t--) {
        int x, y; cin >> x >> y;
        if (abs(x - y) <= 1)
            cout << x + y << endl;
        else
            cout << x + y + (abs(x - y) - 1) << endl;
    }
    return 0;
}
