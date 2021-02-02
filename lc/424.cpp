class Solution {
public:
    int characterReplacement(string s, int k) {
        // slide windows
        vector<int> freq(26);
        int sz = s.size();
        int ptr1 = 0, ptr2 = 0;
        int curMax = 0;

        while (ptr2 < sz) {
            freq[s[ptr2] - 'A']++;
            curMax = max(curMax, freq[s[ptr2] - 'A']);
            if (ptr2 - ptr1 + 1 - curMax > k) {
                freq[s[ptr1] - 'A']--;
                ptr1++;
            }
            ptr2++;
        }
        return ptr2 - ptr1;
    }

};
