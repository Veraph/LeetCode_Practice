class Solution {
public:
    int minimumIncompatibility(vector<int> &nums, int k) {
        int sz = nums.size();
        int subSz = sz / k;

        // edge situation
        // when k == 1 || k == sz
        if (k == 1) {
            set<int> s(nums.begin(), nums.end());
            if (s.size() < sz)
                return -1;
            return (*s.rbegin()) - (*s.begin());
        }

        if (k == n)
            return 0;

        sort(nums.begin(), nums.end());
        // M represents all possiblilities
        // as we have sz numbers, each number
        // can either be used or not 
        int M = (1 << sz), dp[M][sz], cnts[M];
        // calulate the cnts array
        // which cal how many 1's in each number of 
        // cnts
        for (int i = 0; i < M; ++i) {
            int cur = 0;
            for (int j = 0; j < n; ++j) {
                if (i & (1 << j))
                    cur++;
            }
            cnts[i] = cur;
        }
        // initialize the dp matrix
        memset(dp, 0x3f, sizeof(dp));
        memset(dp[0], 0, sizeof(dp[0]));

        // loop through every possibilities
        for (int mask = 1; mask < M; ++mask) {
            // present unused nums are divideable by subSz
            // means we are doing a new sub set
            if ((cnts[mask] % subSz) == 0) {
                // try every available num in nums
                for (int p = 0; p < n; ++p) {
                    // which means the num if usable
                    if (mask & (1 << p)) {
                        // use the smaller one between present val and the val after using p
                        dp[mask][0] = min(dp[mask][0], dp[mask ^ (1 << p)][p]);
                    }
                }
                // update all val with the optimal val at the present state mask
                for (int pre = 1; pre < n; ++pre) {
                    dp[mask][pre] = dp[mask][0];
                }
            // means we are still doing the pre sub set
            // because the nums are sorted
            // hence we only loop the val bigger than pre one in the sub set
            // to avoid duplication
            } else {
                for (int pre = 0; pre < n; ++pre) {
                    for (int p = pre + 1; p < n; ++p) {
                        if ((mask & (1 << p)) && (nums[p] > nums[pre])) {
                            // note
                            // after this operation
                            // every val in the current state (mask) are the same
                            dp[mask][pre] = min(dp[mask][pre], dp[mask ^ (1 << p)][p] + nums[p] - nums[pre]);
                        }
                    }
                }
            }
        }
        // if can not be divided into k sub sets
        if (dp[M - 1][0] >= 10000) {
            return -1;
        }

        return dp[M - 1][0];
    }
};



