#include <iostream>

using namespace::std;

int main() {
    bool numeric = true;

    cout << numeric << endl;

    numeric = numeric || (0 == 1);
    cout << numeric << endl;

    return 0;
}
