class Solution {
public:
    // sort O(nlogn)
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        int zeroCnt = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                zeroCnt++;
            }
        }

        for (int i = zeroCnt + 1; i < nums.size(); i++) {
                if (nums[i] == nums[i - 1]) return false;
                else if (nums[i] - nums[i - 1] == 1) continue;
                else {
                    if (nums[i] - nums[i - 1] > zeroCnt + 1) return false;
                    else {
                        zeroCnt -= (nums[i] - nums[i - 1] - 1);
                        continue;
                    }
                }
        }
        return true;
    }

    // sort optimize
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int joker = 0;
        for (int i = 0; i < 4; i++) {
            if (!nums[i]) joker++;
            else if (nums[i] == nums[i + 1]) return false;
        }
        return nums[4] - nums[joker] < 5;
    }

    // set O(n)
    // but space O(n)
    bool isStraight(vector<int>& nums) {
        set<int> freq;
        int minCard = 14, maxCard = 0;
        for (int i : nums) {
            if (!i) continue;
            minCard = min(minCard, i);
            maxCard = max(maxCard, i);
            if (freq.count(i)) return false;
            freq.insert(i);
        }
        return maxCard - minCard < 5;

    }
};
