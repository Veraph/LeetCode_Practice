// it is actually a fibonacci problem
#include <iostream>
#include <vector>

using namespace::std;

const int MOD = 998244353;

int add(int x, int y) {
    x += y;
    while(x >= MOD) {
        x -= MOD;
    }
    while(x < 0) {
        x += MOD;
    }
    return x;
}

int mul(int x, int y) {
    // trick to cast to long long
    return (x * 1ll * y) % MOD;
}

int biPow(int x, int y) {
    // fast power
    int ans = 1;
    while (y > 0) {
        if (y & 0x1)
            ans = mul(ans, x);
        x = mul(x, x);
        y >>= 1;
    }
    return ans;
}

int divide(int x, int y) {
    return mul(x, biPow(y, MOD - 2));
}

int main() {
    int n; cin >> n;
    vector<int> fib(n + 1);
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; ++i) {
        fib[i] = add(fib[i - 1], fib[i - 2]);
    }

    cout << divide(fib[n], biPow(2, n)) << endl;
    return 0;
}
