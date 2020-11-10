# include <iostream>
# include <vector>

using std::cin, std::cout, std::endl;

int main() {
    int n; cin >> n;
    std::vector <int> a(n);
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    if (a[0] % 2 != a[1] % 2) {
        cout << ((a[2] % 2 == a[0] % 2) ? 2 : 1) << endl;
    } else {
        int flag = a[0] % 2;
        for (int i = 2; i < n; ++i) {
            if (a[i] % 2 != flag) {
                cout << i + 1 << endl;
                break;
            }
        }
    }

    return 0;
}

