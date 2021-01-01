class Solution {
public:
    string reverseWords(string s) {
        istringstream input(s); string tmp;
        string res;
        while(input >> tmp) {
            res = tmp + res;
            res = ' ' + res;
        }
        res.erase(0, 1);
        return res;
    }

    // two pointer
    string reverseWords(string s) {
        string res;
        int right = s.size() - 1;
        while (right >= 0) {
            while(right >= 0 && s[right] == ' ') right--;

            int left = right;
            while (left >= 0 && s[left] != ' ') left--;

            res.append(s.substr(left + 1, right - left) + ' ');
            right = left;
        }

        while (!res.empty() {
            if (res[res.size() - 1] != ' ')
                break;
            else res.pop_back();
        }
        return res;
    }
};
