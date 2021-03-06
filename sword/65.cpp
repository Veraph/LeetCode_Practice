class Solution {
public:
    int add(int a, int b) {
        int sum, carry;
        do {
            sum = a ^ b;
            carry = (unsigned)(a & b) << 1;
            a = sum;
            b = carry;
        } while (b != 0);

        return a;
    }
};
