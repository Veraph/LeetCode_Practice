class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        // 1. build the word map
        unordered_map <int, int> freq;
        for (const string& word : words) {
            int mask = 0;
            for (char ch : word) {
                mask |= (1 << (ch - 'a'));
            }
            
            if (__builtin_popcount(mask) <= 7) ++freq[mask];
        }

        // 2. loop the sub set of puzzles one by one
        vector<int> res;
        for (const string& puzzle : puzzles) {
            int total = 0;
            int mask = 0;

            for (int i = 1; i < 7; i++) {
                mask |= (1 << (puzzle[i] - 'a'));
            }
            int subset = mask;

            // enumerate process
            do {
                // add up the first char
                int s = subset | (1 << (puzzle[0] - 'a'));
                if (freq.count(s)) total += freq[s];
                subset = (subset - 1) & mask;
            } while (subset != mask);

            res.emplace_back(total);
        }

        return res;
    }
};
