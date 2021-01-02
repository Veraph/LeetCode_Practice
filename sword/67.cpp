class Solution {
public:
    int strToInt(string str) {
        int idx = 0, res = 0, limit = INT_MAX / 10, sz = str.size(), sign = 1;

        if (!sz) return 0;
        while (str[idx] == ' ') idx++;
        if (str[idx] == '-') sign = -1;
        if (str[idx] == '-' || str[idx] == '+') idx++;
        for (; idx < sz && (str[idx] >= '0' && str[idx] <= '9'); idx++) {
            // if is 8 and negative, will be INT_MIN instead of -.....
            if (res > limit || res == limit && str[idx] > '7')
                return sign == 1 ? INT_MAX : INT_MIN;
            res = res * 10 + (str[idx] - '0');
        }
        return res * sign;
    }
};
