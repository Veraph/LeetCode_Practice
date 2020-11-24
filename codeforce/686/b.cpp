#include <iostream>
#include <map>

using namespace::std;

int main() {
    int t; cin >> t;
    int nums[200001];
    nums[0] = 200001;
    while (t--) {
        map<int, int> visited;
        int n; cin >> n;
        for (int i = 1; i <= n; ++i) {
            cin >> nums[i];
            visited[nums[i]]++;
        }
        int minIdx = 0;
        for (int i = 1; i <= n; ++i) {
            if (visited[nums[i]] == 1 && nums[i] < nums[minIdx])
                minIdx = i;
        }
        cout << (minIdx == 0 ? -1 : minIdx) << endl;
    }
    return 0;
}



