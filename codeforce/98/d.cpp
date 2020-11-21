#include <iostream>

using namespace::std;

int main() {
    int n; cin >> n;
    double prob = 0.5;
    for (int i = 0; i < n; ++i) {
        prob *= 0.5;
    }
    int base = 1;
    for (int i = 0; i < n; ++i) {
        if (i % 2 != 0)
            base += i;
    }
    
    cout << ((double) base * prob) % (double) 998244353 << endl;

    return 0;
}
