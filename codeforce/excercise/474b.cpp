# include <iostream>

using std::cin, std::cout, std::endl;

int main() {
    int n;
    cin >> n;
    int piles[100001];
    piles[0] = 0;
    int curr;
    for (int i = 1; i <= n; ++i) {
        cin >> curr;
        piles[i] = curr + piles[i - 1];
    }

    int m;
    cin >> m;
    int num;
    for (int i = 0; i < m; ++i) {
        cin >> num;
        // need to use binary search to speed up
        int l = 1, r = n;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (piles[mid] >= num)
                r = mid - 1;
            else
                l = mid + 1;
        }
        cout << l << endl;
    }
    return 0;
}
