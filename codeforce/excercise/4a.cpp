# include <iostream>
# include <algorithm>

using std::cin, std::cout;

int main() {
    int w;
    cin >> w;
    if (w > 2 && (w % 2 == 0))
        cout << "YES" << '\n';
    else
        cout << "NO" << '\n';
    return 0;
}
