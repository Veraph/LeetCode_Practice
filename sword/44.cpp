class Solution {
public:
    int findNthDigit(int n) {
        if (!n) return 0;

        int digit = 1;
        long start = 1, cnt = digit * start * 9;

        while (n > cnt) {
            n -= cnt;
            digit++;
            start *= 10;
            cnt = digit * start * 9;
        }

        // the nth number is at the idx (n - 1)
        long num = start + (n - 1) / digit;
        int remain = (n - 1) % digit;

        string sNum = to_string(num);
        return int(sNum(remain) - '0');
    }
};
