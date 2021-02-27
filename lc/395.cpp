class Solution {
public:
    int longestSubstring(string s, int k) {
        int res = 0;
        int sz = s.size();

        // loop all possibilities of char type
        for (int t = 1; t <= 26; t++) {
            // the left and right bound
            int l = 0, r = 0;
            // the cnt vector
            vector<int> cnt (26, 0);
            // the total to record the types of char
            // the less to record the char doesnt meet k
            int total = 0, less = 0;
            
            // loop the right bound
            while (r < sz) {
                cnt[s[r] - 'a']++;
                if (cnt[s[r] - 'a'] == 1) {
                    total++;
                    less++;
                }

                if (cnt[s[r] - 'a'] == k) less--;
                
                // loop the left bound
                while (total > t) {
                    cnt[s[l] - 'a']--;
                    if (cnt[s[l] - 'a'] == k - 1) less++;

                    if (cnt[s[l] - 'a'] == 0) {
                        total--;
                        less--;
                    }
                    
                    l++;
                }

                // update the res
                if (!less) res = max(res, r - l + 1);
                r++;
            }
        }
        return res;
    }
};
