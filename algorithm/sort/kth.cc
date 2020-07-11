// kth.cc -- find kth largest element
#include <iostream>
#include <vector>
#include <algorithm> //std::nth_element
#include <functional> // std::greater

using std::vector; using std::nth_element; using std::greater;

int main(vector<int> &nums, int k)
{
    // default ascending, use greater to make it descending
    nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
    return nums[k - 1];
}