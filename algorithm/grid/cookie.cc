// cookie.cc -- use grid algorithm to assign cookies
#include <iostream>
#include <algorithm>
#include <vector>
using std::vector; using std::sort;

int main(vector<int> &g, vector<int> &s)
{
    if (g.empty() || s.empty())
        return 0;
    // sort the two vector
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    while (i < g.size() && j < s.size()) {
        if (g[i] <= s[j])
            ++i;
        ++j;
    }
    return i;
}