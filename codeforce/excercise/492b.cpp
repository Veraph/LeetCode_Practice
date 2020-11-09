# include <iostream>
# include <algorithm>
# include <stdio.h>

using std::cin, std::cout, std::endl;

int main() {
    // add 0 and l, and sort the street
    // calculate the differences and get the
    // maximum divide it by 2
    int n, l;
    cin >> n >> l;

    int street[1000];
    for (int i = 0; i < n; ++i) {
        cin >> street[i];
    }

    std::sort(street, street + n);
    double maxDis = 0;

    for (int i = 0; i < n - 1; ++i) {
        maxDis = std::max(maxDis, (street[i + 1] - street[i]) / 2.0);
    }
    
    maxDis = std::max(maxDis, (double) street[0]);
    maxDis = std::max(maxDis, (double) l - street[n - 1]);

    printf("%.5lf\n", maxDis);
    return 0;
}
    


