# include <iostream>

using std::cin, std::cout, std::endl;

int main() {
    int n; cin >> n;
    int nums[100000];
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    
    int start = -1, end = 0, start_val;
    for (int i = 1; i < n; ++i) {
        if (start < 0 && nums[i] < nums[i - 1]) {
            start = i - 1;
            start_val = nums[start];
            for (int j = i + 1; j < n; ++j) {
                if (nums[j] > nums[j - 1]) {
                    end = j - 1;
                    break;
                }
            }
            if (!end)
                end = n - 1;
            break;
        }
    }
    if (start < 0) {
        start = n - 1;
        end = n - 1;
    }

    for (int i = end + 1; i < n; ++i) {
        if (nums[i] < start_val || nums[i] < nums[i - 1]) {
            cout << "no" << endl;
            return 0;
        }
    }
    if ((start != 0) && (nums[end] < nums[start - 1])) {
        cout << "no" << endl;
        return 0;
    }

    cout << "yes" << endl;
    cout << start + 1 << ' ' << end + 1 << endl;
    return 0;
}
