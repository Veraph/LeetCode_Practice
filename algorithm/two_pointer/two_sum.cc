// 167.two_sum.cc -- find two nums in a sorted arrary and make the sum target
#include <iostream>
#include <vector>

using std::cout; using std::endl; using std::vector;

vector<int> main(vector<int> &nums, int target)
{
    int l = 0;
    int r = nums.size() - 1;

    for (int i = 0; i != nums.size() - 1; ++i) {
        if (nums[l] + nums[r] == target)
            return {l, r};
        else if (nums[l] + nums[r] < target)
            ++l;
        else
            --r;

    return {};
    }
}