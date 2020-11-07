# include <iostream>
# include <algorithm>

using std::cin, std::cout, std::endl, std::sort;

int main() {
    int n;
    cin >> n;
    int a[100000];
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    int b[100000];
    for (int i = 0; i < n - 1; ++i) {
        cin >> b[i];
    }
    int c[100000];
    for (int i = 0; i < n - 2; ++i) {
        cin >> c[i];
    }

    sort(a, a + n);
    sort(b, b + n - 1);
    b[n - 1] = -1;
    sort(c, c + n - 2);
    c[n - 2] = -1;
    int first = 0 , second = 0;

    for (int i = 0; i < n; ++i) {
        if (first && second)
            break;
        if (!first && (a[i] != b[i]))
            first = a[i];
        if (!second && (b[i] != c[i]))
            second = b[i];
    }

    cout << first << endl;
    cout << second << endl;
    return 0;
}
