#include <iostream> 
#include <numeric>

using namespace::std;

const int Maxnk = 1000001;
int nums[Maxnk];

int main() {
    int t; cin >> t;
    nums[0] = 0;
    while (t--) {
        long long n, k; cin >> n >> k;
        long long N = n * k;
        for (int i = 1; i <= N; ++i) {
            cin >> nums[i];
        }

        int jmp = n / 2;

        long long res = 0;
        for (int i = 0; i < k; i++) {
            // jmp start from the end
            res += nums[N - jmp - (jmp + 1) * i];
        }
        cout << res << endl;
    }
    return 0;
}


