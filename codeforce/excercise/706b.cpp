# include <iostream>
# include <algorithm>

// when you try to figure out the binary_search problem
// you should be extramelly careful about how the index works
// and to make the problem easier, you can create an array of 100001
// instead of 10000

using std::cin, std::cout, std::endl, std::sort;

int binary_search(int array[], int m, int l, int r) {
    int res = 0;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (array[mid] > m) {
            r = mid - 1;
        } else {
            // even we find the array[mid] == m
            // we still have to loop over the arrary
            // as there may exists many m
            res = mid;
            l = mid + 1;
        }
    }
    return res;
}

int main() {
    int n;
    cin >> n;
    int shops[100001];
    for (int i = 1; i < n + 1; ++i) {
        cin >> shops[i];
    }
    
    sort(shops + 1, shops + n + 1, [](int x, int y) {
            return x < y;
        });

    int q;
    cin >> q;
    while (q--) {
        int m;
        cin >> m;
        cout << binary_search(shops, m, 1, n) << endl;
    }

    return 0;
}

