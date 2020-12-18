// 1. count
// time O(n); space O(set)
class Solution {
public:
    char solve1(string s, string t) {
        vector<int> freq(26, 0);
        for (char c : s)
            freq[c - 'a']++;

        for (char c : s) {
            freq[c - 'a']--;
            if (freq[c - 'a'] < 0)
                return c;
        }
        return ' ';

    }

// 2. sum
// time O(n); space O(1)
    char solve2(string s, string t) {
        int cs = 0, ct = 0;
        for (char c : s)
            cs += c;
        for (char c : t)
            ct += c;

        return ct - cs;
    }

// 3. bit
// time O(n); space O(1)
    char solve3(string s, string t) {
        int ret = 0;
        for (char c : s + t)
            ret ^= c;
        return ret;
    }
};
