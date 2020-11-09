# include <iostream>
# include <algorithm>
using std::cin, std::cout, std::endl;

int main() {
    int n, m, a, b;
    cin >> n >> m >> a >> b;
    int sum1 = INT_MAX;
    int sum2 = INT_MAX;
    // split the situations and calculate
    sum1 = a * n;

    if (m >= n) {
        sum2 = b;
    } else {
        sum2 = 0;
        int bNum = n / m;
        sum2 += (bNum * b);
        int aNeeded = (n - bNum * m) * a;
        sum2 += b > aNeeded ? aNeeded : b;
    }
    
    cout << std::min(sum1, sum2) << endl;
    return 0;
}

        
