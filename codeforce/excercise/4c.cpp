# include <iostream>
# include <string>
# include <map>

using std::cin, std::cout, std::endl;

typedef std::map<std::string, int> database;

int main() {
    int n; cin >> n;
    database d;
    std::string name;
    for (int i = 0; i < n; ++i) {
        cin >> name;
        int r = d[name]++;
        cout << "r:" << r << endl;
        cout << "d[name]:" << d[name] << endl;
        if (!r)
            cout << "OK" << endl;
        else
            cout << name << r << endl;
    }

    return 0;
}
