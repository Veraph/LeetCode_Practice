class Solution {
public:
    bool wordPattern(string pattern, string s) {
        //single hashmap
        map<char, string> help;
        int i = 0;

        for (int j = 0; j < pattern.size() || i < s.size(); j++) {

            if (j >= pattern.size() || i >= s.size()) return false;

            string now = "";
            while (i < s.size() && s[i] != ' ')
                now += s[i++];

            if (help.count(pattern[j])) {
                if (help[pattern[j]] != now)
                    return false;
            } else {
                for (auto it : help) {
                    if (it.second == now)
                        return false;
                }
            }

            help[pattern[j]] = now;
            i++;
        }
        return true;
    }
};
