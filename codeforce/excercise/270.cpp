# include <iostream>

using std::cin, std::cout, std::endl;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a;
        cin >> a;
        if (360 % (180 - a) != 0)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }

    return 0;
}
