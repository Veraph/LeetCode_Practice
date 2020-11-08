# include <iostream>
# include <string>

using std::cin, std::cout, std::endl;

int main() {
    int n;
    cin >> n;
    int num = 5;
    while (n > num) {
        n -= num;
        num *= 2;
    }

    int res;
    res = n / (num / 5);
    if (n % (num / 5) > 0)
        res++;
    
    std::string ans;
    if (res == 1)
        ans = "Sheldon";
    else if (res == 2)
        ans = "Leonard";
    else if (res == 3)
        ans = "Penny";
    else if (res == 4)
        ans = "Rajesh";
    else if (res == 5)
        ans = "Howard";

    cout << ans << endl;

    return 0;
}

