# include <iostream>

using std::cin, std::cout;

int main() {
    long long n, m, a;
    cin >> n >> m >> a;
    long long n_needed, m_needed;
    n_needed += n / a;
    n_needed += n % a ? 1 : 0;
    m_needed += m / a;
    m_needed += m % a ? 1 : 0;

    cout << (n_needed * m_needed) << '\n';
    return 0;
}
