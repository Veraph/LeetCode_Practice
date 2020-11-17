#include <iostream>
#include <vector>
using namespace::std;

int minArrary(vector<int>& numbers) {

    int l = 0;
    int r = numbers.size() - 1;

    while (l <= r) {
         
        int mid = (l + r) / 2;
        if (numbers[mid] > numbers[r]) {
            l = mid + 1;
        } else if (numbers[mid] < numbers[r]) {
            r = mid;
        } else r--;
    }
    return numbers[r];
}
