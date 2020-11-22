// normal solving method
// do not consider the big number
// which can not be represented by long long
class Solution {
public:
    vector<int> printNumbers(int n) {
        vector<int> res;
        long long target = pow(10, n) - 1;
        for(long long i = 1; i <= target; ++i) {
            res.push_back(i);
        }
        return res;
    }
};

// consider the big number
// simulate add on string
class Solution {
public:
    vector<int> printNumbers(int n) {
        if (n <= 0)
            return vector<int> (0);
        vector<int> res;
        string num (n, '0');

        while (!increment(num))
            putIn(res, num);

        return res;
    }

    bool increment(string &s) {
        bool isOver = false;
        int carry = 0;
        int numLen = s.size();

        for (int i = numLen - 1; i >= 0; i--) {
            int cur = s[i] - '0' + carry;
            if (i == numLen - 1)
                cur++;

            if (cur >= 10) {
                if (i == 0)
                    isOver = true;
                else {
                    cur -= 10;
                    carry = 1;
                    s[i] = '0' + cur;
                }
            } else {
                s[i] = '0' + cur;
                break;
            }
        }

        return isOver;
    }

    void putIn(vector<int> &res, string &s) {
        bool beginZero = true;
        int numLen = s.size();
        string temp;
        for (int i = 0; i < numLen; i++) {
            if (beginZero && s[i] != '0')
                beginZero = false;
            if (!beginZero)
               temp.push_back(s[i]);
        }
        // in the interview we just pusb_back the
        // original string as we will set the elemnet
        // of res as string
        res.push_back(stoi(temp));
    }
};


// Recursive method
// this is actually a full permutation
class Solution {
public:
    vector<int> printNumbers(int n) {
        if (n <= 0)
            return vector<int> (0);

        vector<int> res;
        string s (n, '0');

        dfs(s, res, 0);

        return res;
    }

    void dfs(string &s, vector<int> &res, int idx) {
        if (idx == s.size()) {
            putIn(s, res);
            return;
        }

        for (int i = 0; i < 10; i++) {
            s[idx] = '0' + i;
            dfs(s, res, idx + 1);
        }
    }

    void putIn(string &s, vector<int> &res) {
        bool beginZero = true;
        string temp;
        for (int i = 0; i < s.size(); i++) {
            if (beginZero && s[i] != '0')
                beginZero = false;
            if (!beginZero) 
                temp.push_back(s[i]);
        }
        // stoi will arise error if temp is "0000.."
        if (temp != "")
            res.push_back(stoi(temp));
    }
};

