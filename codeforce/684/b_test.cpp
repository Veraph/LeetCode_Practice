#include <iostream> 
#include <numeric>
 
using namespace::std;
 
const int Maxnk = 1000001;
long long nums[Maxnk];
long long init = 0;

int main() {
    int t; cin >> t;
    nums[0] = 0;
    while (t--) {
        long long n, k; cin >> n >> k;
        long long N = n * k;

        for (long long i = 1; i <= N; ++i) {
            cin >> nums[i];
        }
 
        if (n == 1) {
            // the return type of accumulate will based on the init!!!
            cout << accumulate(nums + 1, nums + k + 1, init) << endl;
            continue;
        } else if (k == 1) {
            cout << nums[((n - 1) >> 1) + 1] << endl;
            continue;
        }
 
        long long mul = 0;
        if (n % 2 == 0) {
            mul = n / 2 - 1;
        } else {
            mul = n / 2;
        }
        long long skip = n - mul;
        long long res = 0;
        for (long long i = mul * k + 1; i <= n * k; i += skip) {
            res += nums[i];
        }
        cout << res << endl;
    }
    return 0;
}
 
 
