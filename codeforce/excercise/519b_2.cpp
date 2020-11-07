# include <iostream>

using std::cin, std::cout, std::endl;

int main() {
    int n;
    cin >> n;
    int sum_a = 0, sum_b = 0, sum_c = 0;
    int temp_a, temp_b, temp_c;
    for (int i = 0; i < n; ++i) {
        cin >> temp_a;
        sum_a += temp_a;
    }
    for (int i = 0; i < n - 1; ++i) {
        cin >> temp_b;
        sum_b += temp_b;
    }
    for (int i = 0; i < n - 2; ++i) {
        cin >> temp_c;
        sum_c += temp_c;
    }

    cout << sum_a - sum_b << endl;
    cout << sum_b - sum_c << endl;

    return 0;
}
        
