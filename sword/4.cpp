# include <iostream>
# include <string>

class Solution {
    public:
        string func(string s) {
            
            //loop the string first time to
            //make sure how many space we have
            int numBlank = 0;
            for (int i = 0; i < s.size(); ++i) {
                if (s[i] == ' ')
                    numBlank++;
            }
            int newLen = s.size() + numBlank * 2;
            int oldLen = s.size();
            // resize the array
            s.resize(newLen);
            while (oldLen >= 0 && newLen > oldLen) {
                if (s[oldLen] == ' ') {
                    s[newLen--] = '0';
                    s[newLen--] = '2';
                    s[newLen--] = '%';
                } else {
                    s[newLen--] = s[oldLen];
                }

                --oldLen;
        }
};
