# include <iostream>
# include <cmath>
# include <bitset>
# define maxNum 1000001

using std::cin, std::cout, std::endl;


int main() {
    // bitset idx start from right to left
    std::bitset <maxNum> not_prime;
    not_prime.set(0);
    not_prime.set(1);
    for (int i = 2; i * i < maxNum; ++i) {
        if (!not_prime[i]) {
            for (int j = i * i; j < maxNum; j += i)
                not_prime[j] = 1;
        }
    }

    int n; cin >> n;
    for (int i = 0; i < n; ++i) {
        long long num; cin >> num;
        long long num_sqrt = sqrt(num);
        if ((num_sqrt * num_sqrt == num) && (!not_prime[num_sqrt]))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}

