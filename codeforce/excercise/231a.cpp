# include <iostream>
using std::cin, std::cout;

int main() {
    int n;
    cin >> n;
    int ans = 0;
    while (n--) {
        int a, b, c;
        cin >> a >> b >> c;
        if ((a + b + c) > 1)
            ans++;
    }
    cout << ans << '\n';
    return 0;
}
