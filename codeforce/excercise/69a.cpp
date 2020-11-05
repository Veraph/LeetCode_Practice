# include <iostream>
using std::cin, std::cout;

int main() {
    int n;
    cin >> n;
    int x = 0, y = 0, z = 0;
    int temp_x, temp_y, temp_z;
    while (n--) {
        cin >> temp_x >> temp_y >> temp_z;
        x += temp_x;
        y += temp_y;
        z += temp_z;
    }
    if (x == 0 && y == 0 && z == 0)
        cout << "YES" << '\n';
    else
        cout << "NO" << '\n';
    
    return 0;
}
