class Solution {
public:
    // count the 1 in every digits
    int countDigitOne(int n) {
        long digit = 1; int res = 0;
        int high = n / 10, low = 0, cur = n % 10;
        while (high || cur) {
            if (!cur) res += high * digit;
            else if (cur == 1) res += high * digit + low + 1;
            else res += (high + 1) * digit;
            
            low += cur * digit;
            cur = high % 10;
            high /= 10; 
            digit *= 10;
        }
        return res;
    }
};
