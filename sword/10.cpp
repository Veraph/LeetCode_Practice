#include <iostream>

using namespace::std;

long long fib(unsigned n) {
    int ini[2] = {0, 1};
    if (n < 2) 
        return ini[n];

    long long pre1 = 1;
    long long pre2 = 0;
    long long fib = 0;
    for (unsigned int i = 2; i <= n; ++i) {
        fib = pre1 + pre2;
        pre2 = pre1;
        pre1 = fib;
    }
    return fib;
}
