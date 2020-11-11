# include <iostream>
# include <algorithm>

using std::cin, std::cout, std::endl;

int main() {
    // do not need to sort
    // if it is the maximum or minimum
    // then it will never be influenced
    int n; cin >> n;
    int min = INT_MAX, max = 0, minCnt, maxCnt, x;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x < min) {
            min = x;
            minCnt = 1;
        } else if (x == min)
            minCnt++;

        if (x > max) {
            max = x;
            maxCnt = 1;
        } else if (x == max)
            maxCnt++;
    }

    if (min == max)
        cout << 0 << ' ' << (long long) n * (n - 1) / 2 << endl;
    else
        cout << max - min << ' ' << (long long) minCnt * maxCnt << endl;

    return 0;
}
                
