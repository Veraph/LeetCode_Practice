// sqrt.cc -- an example to ilustrate binary search
#include <iostream>

int main(int x)
{
    if (x <= 1)
        return x;  
    int l = 0, r = x;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        int sqrt = x / mid;
        if (sqrt == mid)
            return mid;
        else if (sqrt < mid)
            r = mid - 1;
        else
            l = mid + 1;
    }
    return r;
}