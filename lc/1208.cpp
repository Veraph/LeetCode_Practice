class Solution {
public:
    // 1. window sliding
    // time O(n)
    // space O(n) but could be O(1) if we calculate abs in the sliding loop
    int equalSubstring(string s, string t, int maxCost) {
        // 1. build aux vector
        int sz = s.size();
        vector<int> cost(sz);
        for (int i = 0; i < sz; i++) {
            cost[i] = abs(s[i] - t[i]);
        }

        // 2. do the sliding
        int left = 0, right = 0, maxLen = 0, curSum = 0;
        while (right < sz) {
            curSum += cost[right];
            
            while (curSum > maxCost) {
                curSum -= cost[left++];
            }

            right++;
            maxLen = max(maxLen, right - left);
        }
        return maxLen;
    }
    
    // 2. binary serach
    // time O(nlogn), space o(n)
    int binarySearch(const vector<int>& acCost, int end, int target) {
        int left = 0, right = end;
        while (left <= end) {
            // we should find the idx that >= than the target
            // which is the smallest left idx
            int mid = left + (right - left) / 2;
            if (acCost[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    int equalSubstring(string s, string t, int maxCost) {
        in sz = s.size();
        vector<int> acCost(sz + 1, 0);

        // 1. build the acCost vector
        for (int i = 1; i <= sz; i++) {
            acCost[i] = acCost[i - 1] + abs(s[i - 1] - t[i - 1]);
        }

        // 2. do the binary search
        int maxLen = 0;
        for (int end = 1; end <= sz; end++) {
            int start = binarySearch(acCost, end, acCost[i] - maxCost);
            maxLen = max(maxLen, end - start);
        }

        return maxLen;
    }
};
