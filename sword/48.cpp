class Solution {
public:
    // dp
    // time O(n) space O(n)
   int lengthOfLongestSubstring(string s) {
        vector<int> aux(26, -1);
        int cur = 0, res = 0;
        for (int i = 0; i < s.size(); i++) {
            // the second condition means even the s[i] appreared before
            // but will not influence the present sub str.
            if (aux[s[i] - 'a'] < 0 || i - aux[s[i] - 'a'] > cur) {
                cur++;
            } else {
                res = max(res, cur);
                cur = i - aux[s[i] - 'a'];
            }
            aux[s[i] - 'a'] = i;
        }
        return max(res, cur);
    }

    // slide windows
    int lengthOfLongestSubstring(string s) {
        map<char, int> aux;
        int start = -1, res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (aux.count(s[i]))
                // have to get the max to avoid the other duplication
                // apart from s[i] itself.
                    start = max(start, aux[s[i]]);
            aux[s[i]] = i;
            res = max(res, i - start);
        }
        return res;
    }
};
