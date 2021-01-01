class Solution {
public:
    // method 1
    // string slice
    string reverseLeftWords(string s, int n) {
        return s.substr(n, s.size() - n) + s.substr(0, n);
    }

    // method 2
    // build a new one
    string reverseLeftWords(string s, int n) {
        string res;
        for (int i = n; i < s.size(); i++) {
            res.push_back(s[i]);
        }

        for (int i = 0; i < n; i++) {
            res.push_back(s[i]);
        }
        return res;
    }

    // method 2 optimize
    string reverseLeftWords(string s, int n) {
        string res;
        for (int i = n; i < n + s.size(); i++) {
            res.push_back(s[i % s.size()]);
        }
        return res;
    }

    // method 3
    // triple reverse
    string reverseLeftWords(string s, int n) {
        if (s.size() < 2)
            return s;

        reverse(s, 0, n - 1);
        reverse(s, n, s.size() - 1);
        reverse(s, 0, s.size() - 1);
        return s;
    }
    
    void reverse(string &s, int start, int end) {
        while (start < end) {
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++; end--;
        }

    }
};
